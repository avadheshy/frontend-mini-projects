from datetime import datetime
import secrets

from bson import ObjectId
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.api.deps import get_current_user, get_db
from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.mail.templates.email_verification_template import otp_template
from app.mail.templates.password_update import password_updated
from app.schemas.auth import (
    ChangePasswordRequest,
    LoginRequest,
    ResetPasswordRequest,
    ResetPasswordTokenRequest,
    SendOtpRequest,
    SignupRequest,
)
from app.utils.mail_sender import send_mail
from app.utils.mongo import with_string_id

router = APIRouter()


def _generate_otp() -> str:
    return "".join(secrets.choice("0123456789") for _ in range(6))


@router.post("/signup")
async def signup(payload: SignupRequest, db=Depends(get_db)):
    if (
        not payload.firstName
        or not payload.lastName
        or not payload.email
        or not payload.password
        or not payload.confirmPassword
        or not payload.otp
    ):
        raise HTTPException(status_code=403, detail="All Fields are required")

    if payload.password != payload.confirmPassword:
        raise HTTPException(
            status_code=400,
            detail="Password and Confirm Password do not match. Please try again.",
        )

    existing_user = await db.users.find_one({"email": payload.email})
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists. Please sign in to continue.",
        )

    otp_doc = (
        await db.otps.find({"email": payload.email})
        .sort("createdAt", -1)
        .limit(1)
        .to_list(length=1)
    )
    if not otp_doc:
        raise HTTPException(status_code=400, detail="The OTP is not valid")
    if payload.otp != otp_doc[0].get("otp"):
        raise HTTPException(status_code=400, detail="The OTP is not valid")

    hashed_password = get_password_hash(payload.password)

    approved = False if payload.accountType == "Instructor" else True

    profile_result = await db.profiles.insert_one(
        {
            "gender": None,
            "dateOfBirth": None,
            "about": None,
            "contactNumber": None,
        }
    )

    user_doc = {
        "firstName": payload.firstName,
        "lastName": payload.lastName,
        "email": payload.email,
        "contactNumber": payload.contactNumber,
        "password": hashed_password,
        "accountType": payload.accountType,
        "approved": approved,
        "additionalDetails": profile_result.inserted_id,
        "image": "",
        "active": True,
        "courses": [],
        "courseProgress": [],
    }

    user_result = await db.users.insert_one(user_doc)
    created = await db.users.find_one({"_id": user_result.inserted_id})

    return {
        "success": True,
        "user": with_string_id(created),
        "message": "User registered successfully",
    }


@router.post("/login")
async def login(payload: LoginRequest, response: Response, db=Depends(get_db)):
    if not payload.email or not payload.password:
        raise HTTPException(
            status_code=400, detail="Please Fill up All the Required Fields"
        )

    user = await db.users.find_one({"email": payload.email})
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User is not Registered with Us Please SignUp to Continue",
        )

    if not verify_password(payload.password, user.get("password")):
        raise HTTPException(status_code=401, detail="Password is incorrect")

    token = create_access_token(
        {
            "email": user.get("email"),
            "id": str(user.get("_id")),
            "role": user.get("accountType"),
            "accountType": user.get("accountType"),
        }
    )

    await db.users.update_one({"_id": user["_id"]}, {"$set": {"token": token}})
    user["password"] = None
    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        max_age=3 * 24 * 60 * 60,
    )

    return {
        "success": True,
        "token": token,
        "user": with_string_id(user),
        "message": "User Login Success",
    }


@router.post("/sendotp")
async def send_otp(payload: SendOtpRequest, db=Depends(get_db)):
    check_user = await db.users.find_one({"email": payload.email})
    if check_user:
        raise HTTPException(status_code=401, detail="User is Already Registered")

    otp = _generate_otp()
    while await db.otps.find_one({"otp": otp}):
        otp = _generate_otp()

    await db.otps.insert_one(
        {"email": payload.email, "otp": otp, "createdAt": datetime.utcnow()}
    )

    try:
        send_mail(payload.email, "Verification Email", otp_template(otp))
    except Exception as e:
        print("Email error:", e)
        raise HTTPException(status_code=500, detail=str(e))

    return {"success": True, "message": "OTP Sent Successfully", "otp": otp}


@router.post("/changepassword")
async def change_password(
    payload: ChangePasswordRequest,
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    user_details = await db.users.find_one({"_id": ObjectId(user["id"])})
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(payload.oldPassword, user_details.get("password")):
        raise HTTPException(status_code=401, detail="The password is incorrect")

    encrypted_password = get_password_hash(payload.newPassword)
    await db.users.update_one(
        {"_id": user_details["_id"]}, {"$set": {"password": encrypted_password}}
    )

    try:
        send_mail(
            user_details["email"],
            "Password for your account has been updated",
            password_updated(
                user_details["email"],
                f"Password updated successfully for {user_details.get('firstName', '')} {user_details.get('lastName', '')}",
            ),
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error occurred while sending email: {exc}",
        )

    return {"success": True, "message": "Password updated successfully"}


@router.post("/reset-password-token")
async def reset_password_token(payload: ResetPasswordTokenRequest, db=Depends(get_db)):
    user = await db.users.find_one({"email": payload.email})
    if not user:
        return {
            "success": False,
            "message": f"This Email: {payload.email} is not Registered With Us Enter a Valid Email ",
        }

    token = secrets.token_hex(20)
    await db.users.update_one(
        {"_id": user["_id"]},
        {
            "$set": {
                "token": token,
                "resetPasswordExpires": datetime.utcnow() + timedelta(hours=1),
            }
        },
    )

    reset_url = f"{settings.frontend_reset_url}/{token}"
    try:
        send_mail(
            payload.email,
            "Password Reset",
            f"Your Link for email verification is {reset_url}. Please click this url to reset your password.",
        )
    except Exception:
        pass

    return {
        "success": True,
        "message": "Email Sent Successfully, Please Check Your Email to Continue Further",
    }


@router.post("/reset-password")
async def reset_password(payload: ResetPasswordRequest, db=Depends(get_db)):
    if payload.confirmPassword != payload.password:
        return {
            "success": False,
            "message": "Password and Confirm Password Does not Match",
        }

    user_details = await db.users.find_one({"token": payload.token})
    if not user_details:
        return {"success": False, "message": "Token is Invalid"}

    if not (user_details.get("resetPasswordExpires", datetime.min) > datetime.utcnow()):
        raise HTTPException(
            status_code=403,
            detail="Token is Expired, Please Regenerate Your Token",
        )

    encrypted_password = get_password_hash(payload.password)
    await db.users.update_one(
        {"_id": user_details["_id"]}, {"$set": {"password": encrypted_password}}
    )

    return {"success": True, "message": "Password Reset Successful"}
