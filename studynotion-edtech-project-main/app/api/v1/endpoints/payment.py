import hashlib
import hmac
import random

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from pymongo import ReturnDocument

from app.api.deps import get_current_user, get_db, require_role
from app.core.config import settings
from app.core.razorpay import get_razorpay_client
from app.mail.templates.course_enrollment_email import course_enrollment_email
from app.mail.templates.payment_success_email import payment_success_email
from app.schemas.payment import (
    CapturePaymentRequest,
    PaymentSuccessEmailRequest,
    VerifyPaymentRequest,
)
from app.utils.mail_sender import send_mail

router = APIRouter()


@router.post("/capturePayment")
async def capture_payment(
    payload: CapturePaymentRequest,
    user=Depends(get_current_user),
    _role=Depends(require_role("Student")),
    db=Depends(get_db),
):
    if not payload.courses:
        return {"success": False, "message": "Please Provide Course ID"}

    total_amount = 0

    for course_id in payload.courses:
        course = await db.courses.find_one({"_id": ObjectId(course_id)})
        if not course:
            return {"success": False, "message": "Could not find the Course"}

        if ObjectId(user["id"]) in course.get("studentsEnroled", []):
            return {"success": False, "message": "Student is already Enrolled"}

        total_amount += course.get("price", 0)

    options = {
        "amount": int(total_amount * 100),
        "currency": "INR",
        "receipt": str(random.random()),
    }

    try:
        client = get_razorpay_client()
        payment_response = client.order.create(options)
        return {"success": True, "data": payment_response}
    except Exception:
        raise HTTPException(status_code=500, detail="Could not initiate order.")


@router.post("/verifyPayment")
async def verify_payment(
    payload: VerifyPaymentRequest,
    user=Depends(get_current_user),
    _role=Depends(require_role("Student")),
    db=Depends(get_db),
):
    if not (
        payload.razorpay_order_id
        and payload.razorpay_payment_id
        and payload.razorpay_signature
        and payload.courses
        and user
    ):
        return {"success": False, "message": "Payment Failed"}

    body = f"{payload.razorpay_order_id}|{payload.razorpay_payment_id}"
    expected_signature = hmac.new(
        settings.razorpay_secret.encode(), body.encode(), hashlib.sha256
    ).hexdigest()

    if expected_signature == payload.razorpay_signature:
        await _enroll_students(payload.courses, user["id"], db)
        return {"success": True, "message": "Payment Verified"}

    return {"success": False, "message": "Payment Failed"}


@router.post("/sendPaymentSuccessEmail")
async def send_payment_success_email(
    payload: PaymentSuccessEmailRequest,
    user=Depends(get_current_user),
    _role=Depends(require_role("Student")),
    db=Depends(get_db),
):
    if not (payload.orderId and payload.paymentId and payload.amount and user):
        raise HTTPException(status_code=400, detail="Please provide all the details")

    enrolled_student = await db.users.find_one({"_id": ObjectId(user["id"])})
    if not enrolled_student:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        send_mail(
            enrolled_student["email"],
            "Payment Received",
            payment_success_email(
                f"{enrolled_student.get('firstName', '')} {enrolled_student.get('lastName', '')}",
                payload.amount / 100,
                payload.orderId,
                payload.paymentId,
            ),
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Could not send email")

    return {"success": True}


async def _enroll_students(courses: list[str], user_id: str, db) -> None:
    if not courses or not user_id:
        raise HTTPException(
            status_code=400, detail="Please Provide Course ID and User ID"
        )

    for course_id in courses:
        enrolled_course = await db.courses.find_one_and_update(
            {"_id": ObjectId(course_id)},
            {"$push": {"studentsEnroled": ObjectId(user_id)}},
            return_document=ReturnDocument.AFTER,
        )

        if not enrolled_course:
            raise HTTPException(status_code=500, detail="Course not found")

        course_progress = await db.courseprogresses.insert_one(
            {
                "courseID": ObjectId(course_id),
                "userId": ObjectId(user_id),
                "completedVideos": [],
            }
        )

        enrolled_student = await db.users.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {
                "$push": {
                    "courses": ObjectId(course_id),
                    "courseProgress": course_progress.inserted_id,
                }
            },
            return_document=ReturnDocument.AFTER,
        )

        if enrolled_student:
            try:
                send_mail(
                    enrolled_student["email"],
                    f"Successfully Enrolled into {enrolled_course.get('courseName')}",
                    course_enrollment_email(
                        enrolled_course.get("courseName", ""),
                        f"{enrolled_student.get('firstName', '')} {enrolled_student.get('lastName', '')}",
                    ),
                )
            except Exception:
                pass
