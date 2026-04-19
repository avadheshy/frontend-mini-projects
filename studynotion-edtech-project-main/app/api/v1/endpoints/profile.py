from bson import ObjectId
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.api.deps import get_current_user, get_db, require_role
from app.core.config import settings
from app.schemas.profile import UpdateProfileRequest
from app.utils.image_uploader import upload_image_to_cloudinary
from app.utils.mongo import with_string_id
from app.utils.sec_to_duration import convert_seconds_to_duration

router = APIRouter()


@router.put("/updateProfile")
async def update_profile(
    payload: UpdateProfileRequest,
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    user_id = ObjectId(user["id"])
    user_details = await db.users.find_one({"_id": user_id})
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")

    await db.users.update_one(
        {"_id": user_id},
        {"$set": {"firstName": payload.firstName, "lastName": payload.lastName}},
    )

    profile_id = user_details.get("additionalDetails")
    if profile_id:
        await db.profiles.update_one(
            {"_id": profile_id},
            {
                "$set": {
                    "dateOfBirth": payload.dateOfBirth,
                    "about": payload.about,
                    "contactNumber": payload.contactNumber,
                    "gender": payload.gender,
                }
            },
        )

    updated_user = await db.users.find_one({"_id": user_id})
    if profile_id:
        profile = await db.profiles.find_one({"_id": profile_id})
        updated_user["additionalDetails"] = with_string_id(profile)

    return {
        "success": True,
        "message": "Profile updated successfully",
        "updatedUserDetails": with_string_id(updated_user),
    }


@router.delete("/deleteProfile")
async def delete_account(user=Depends(get_current_user), db=Depends(get_db)):
    user_id = ObjectId(user["id"])
    user_details = await db.users.find_one({"_id": user_id})
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")

    profile_id = user_details.get("additionalDetails")
    if profile_id:
        await db.profiles.delete_one({"_id": profile_id})

    for course_id in user_details.get("courses", []):
        await db.courses.update_one(
            {"_id": course_id}, {"$pull": {"studentsEnroled": user_id}}
        )

    await db.users.delete_one({"_id": user_id})
    await db.courseprogresses.delete_many({"userId": user_id})

    return {"success": True, "message": "User deleted successfully"}


@router.get("/getUserDetails")
async def get_all_user_details(user=Depends(get_current_user), db=Depends(get_db)):
    user_id = ObjectId(user["id"])
    user_details = await db.users.find_one({"_id": user_id})
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")

    profile_id = user_details.get("additionalDetails")
    if profile_id:
        profile = await db.profiles.find_one({"_id": profile_id})
        user_details["additionalDetails"] = with_string_id(profile)

    return {
        "success": True,
        "message": "User Data fetched successfully",
        "data": with_string_id(user_details),
    }


@router.put("/updateDisplayPicture")
async def update_display_picture(
    displayPicture: UploadFile = File(...),
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    user_id = ObjectId(user["id"])
    image = upload_image_to_cloudinary(displayPicture, settings.cloud_folder, 1000, 1000)

    await db.users.update_one(
        {"_id": user_id}, {"$set": {"image": image.get("secure_url")}}
    )
    updated_profile = await db.users.find_one({"_id": user_id})

    return {
        "success": True,
        "message": "Image Updated successfully",
        "data": with_string_id(updated_profile),
    }


@router.get("/getEnrolledCourses")
async def get_enrolled_courses(user=Depends(get_current_user), db=Depends(get_db)):
    user_id = ObjectId(user["id"])
    user_details = await db.users.find_one({"_id": user_id})
    if not user_details:
        raise HTTPException(status_code=400, detail="Could not find user")

    courses = []
    for course_id in user_details.get("courses", []):
        course = await db.courses.find_one({"_id": course_id})
        if not course:
            continue

        course_content = []
        for section_id in course.get("courseContent", []):
            section = await db.sections.find_one({"_id": section_id})
            if not section:
                continue
            subsections = []
            for sub_id in section.get("subSection", []):
                sub = await db.subsections.find_one({"_id": sub_id})
                if sub:
                    subsections.append(with_string_id(sub))
            section["subSection"] = subsections
            course_content.append(with_string_id(section))

        course["courseContent"] = course_content

        total_duration_seconds = 0
        subsection_length = 0
        for content in course_content:
            total_duration_seconds += sum(
                int(sub.get("timeDuration", 0)) for sub in content.get("subSection", [])
            )
            subsection_length += len(content.get("subSection", []))

        course["totalDuration"] = convert_seconds_to_duration(total_duration_seconds)

        course_progress = await db.courseprogresses.find_one(
            {"courseID": course["_id"], "userId": user_id}
        )
        completed_count = len(course_progress.get("completedVideos", [])) if course_progress else 0
        if subsection_length == 0:
            course["progressPercentage"] = 100
        else:
            course["progressPercentage"] = round((completed_count / subsection_length) * 100, 2)

        courses.append(with_string_id(course))

    return {"success": True, "data": courses}


@router.get("/instructorDashboard")
async def instructor_dashboard(
    user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    instructor_id = ObjectId(user["id"])
    course_details = await db.courses.find({"instructor": instructor_id}).to_list(length=None)

    course_data = []
    for course in course_details:
        total_students_enrolled = len(course.get("studentsEnroled", []))
        total_amount_generated = total_students_enrolled * course.get("price", 0)
        course_data.append(
            {
                "_id": str(course.get("_id")),
                "courseName": course.get("courseName"),
                "courseDescription": course.get("courseDescription"),
                "totalStudentsEnrolled": total_students_enrolled,
                "totalAmountGenerated": total_amount_generated,
            }
        )

    return {"courses": course_data}
