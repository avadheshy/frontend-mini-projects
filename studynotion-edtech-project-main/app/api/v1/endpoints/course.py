import json
from datetime import datetime
from typing import Any

from bson import ObjectId
from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile

from app.api.deps import get_current_user, get_db, require_role
from app.schemas.course import (
    CategoryPageDetailsRequest,
    CourseIdRequest,
    CreateCategoryRequest,
    CreateRatingRequest,
    CreateSectionRequest,
    CreateSubSectionRequest,
    DeleteSectionRequest,
    DeleteSubSectionRequest,
    UpdateCourseProgressRequest,
    UpdateSectionRequest,
    UpdateSubSectionRequest,
)
from app.core.config import settings
from app.utils.image_uploader import upload_image_to_cloudinary
from app.utils.mongo import with_string_id
from app.utils.sec_to_duration import convert_seconds_to_duration

router = APIRouter()


def _oid(value: str) -> ObjectId:
    return ObjectId(value)


def _stringify_list(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [with_string_id(item) for item in items]


def _ensure_course_instructor(db, course_id: ObjectId, instructor_id: ObjectId):
    return db.courses.find_one({"_id": course_id, "instructor": instructor_id})


@router.post("/createCourse")
async def create_course(
    courseName: str = Form(...),
    courseDescription: str = Form(...),
    whatYouWillLearn: str = Form(...),
    price: float = Form(...),
    tag: str = Form(...),
    category: str = Form(...),
    instructions: str = Form(...),
    status: str | None = Form(None),
    thumbnailImage: UploadFile = File(...),
    user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    instructor_id = ObjectId(user["id"])

    tags = json.loads(tag)
    instructions_list = json.loads(instructions)

    if (
        not courseName
        or not courseDescription
        or not whatYouWillLearn
        or not price
        or not tags
        or not thumbnailImage
        or not category
        or not instructions_list
    ):
        raise HTTPException(status_code=400, detail="All Fields are Mandatory")

    if not status:
        status = "Draft"

    instructor_details = await db.users.find_one(
        {"_id": instructor_id, "accountType": "Instructor"}
    )
    if not instructor_details:
        raise HTTPException(status_code=404, detail="Instructor Details Not Found")

    category_details = await db.categories.find_one({"_id": _oid(category)})
    if not category_details:
        raise HTTPException(status_code=404, detail="Category Details Not Found")

    thumbnail = upload_image_to_cloudinary(thumbnailImage, settings.cloud_folder)

    new_course = {
        "courseName": courseName,
        "courseDescription": courseDescription,
        "instructor": instructor_id,
        "whatYouWillLearn": whatYouWillLearn,
        "price": price,
        "tag": tags,
        "category": category_details["_id"],
        "thumbnail": thumbnail.get("secure_url"),
        "status": status,
        "instructions": instructions_list,
        "courseContent": [],
        "ratingAndReviews": [],
        "studentsEnroled": [],
        "createdAt": datetime.utcnow(),
    }

    course_result = await db.courses.insert_one(new_course)

    await db.users.update_one(
        {"_id": instructor_id}, {"$push": {"courses": course_result.inserted_id}}
    )
    await db.categories.update_one(
        {"_id": category_details["_id"]},
        {"$push": {"courses": course_result.inserted_id}},
    )

    created_course = await db.courses.find_one({"_id": course_result.inserted_id})

    return {
        "success": True,
        "data": with_string_id(created_course),
        "message": "Course Created Successfully",
    }


@router.post("/editCourse")
async def edit_course(
    request: Request,
    user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    form = await request.form()
    course_id = form.get("courseId")
    if not course_id:
        raise HTTPException(status_code=400, detail="Course not found")

    course = await db.courses.find_one({"_id": _oid(course_id)})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    updates: dict[str, Any] = {}
    for key, value in form.items():
        if key == "courseId":
            continue
        if key in {"tag", "instructions"}:
            updates[key] = json.loads(value)
        elif key == "thumbnailImage" and hasattr(value, "filename"):
            upload = upload_image_to_cloudinary(value, settings.cloud_folder)
            updates["thumbnail"] = upload.get("secure_url")
        else:
            updates[key] = value

    if updates:
        await db.courses.update_one({"_id": _oid(course_id)}, {"$set": updates})

    updated_course = await _get_full_course(db, _oid(course_id), include_video=True)

    return {
        "success": True,
        "message": "Course updated successfully",
        "data": updated_course,
    }


@router.get("/getAllCourses")
async def get_all_courses(db=Depends(get_db)):
    courses = await db.courses.find({"status": "Published"}).to_list(length=None)

    for course in courses:
        instructor = await db.users.find_one({"_id": course.get("instructor")})
        course["instructor"] = with_string_id(instructor)

    return {"success": True, "data": _stringify_list(courses)}


@router.post("/getCourseDetails")
async def get_course_details(payload: CourseIdRequest, db=Depends(get_db)):
    course_details = await _get_full_course(
        db, _oid(payload.courseId), include_video=False
    )

    if not course_details:
        raise HTTPException(
            status_code=400,
            detail=f"Could not find course with id: {payload.courseId}",
        )

    total_duration_seconds = 0
    for content in course_details.get("courseContent", []):
        for sub in content.get("subSection", []):
            total_duration_seconds += int(sub.get("timeDuration", 0))

    total_duration = convert_seconds_to_duration(total_duration_seconds)

    return {
        "success": True,
        "data": {"courseDetails": course_details, "totalDuration": total_duration},
    }


@router.post("/getFullCourseDetails")
async def get_full_course_details(
    payload: CourseIdRequest,
    user=Depends(get_current_user),
    db=Depends(get_db),
):
    course_details = await _get_full_course(
        db, _oid(payload.courseId), include_video=True
    )

    if not course_details:
        raise HTTPException(
            status_code=400,
            detail=f"Could not find course with id: {payload.courseId}",
        )

    total_duration_seconds = 0
    for content in course_details.get("courseContent", []):
        for sub in content.get("subSection", []):
            total_duration_seconds += int(sub.get("timeDuration", 0))

    total_duration = convert_seconds_to_duration(total_duration_seconds)

    course_progress = await db.courseprogresses.find_one(
        {"courseID": _oid(payload.courseId), "userId": ObjectId(user["id"])}
    )
    completed_videos = course_progress.get("completedVideos", []) if course_progress else []

    return {
        "success": True,
        "data": {
            "courseDetails": course_details,
            "totalDuration": total_duration,
            "completedVideos": [str(vid) for vid in completed_videos] if completed_videos else [],
        },
    }


@router.get("/getInstructorCourses")
async def get_instructor_courses(
    user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    instructor_id = ObjectId(user["id"])
    instructor_courses = (
        await db.courses.find({"instructor": instructor_id})
        .sort("createdAt", -1)
        .to_list(length=None)
    )
    return {"success": True, "data": _stringify_list(instructor_courses)}


@router.delete("/deleteCourse")
async def delete_course(payload: CourseIdRequest, db=Depends(get_db)):
    course = await db.courses.find_one({"_id": _oid(payload.courseId)})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    for student_id in course.get("studentsEnroled", []):
        await db.users.update_one(
            {"_id": student_id}, {"$pull": {"courses": course["_id"]}}
        )

    for section_id in course.get("courseContent", []):
        section = await db.sections.find_one({"_id": section_id})
        if section:
            await db.subsections.delete_many({"_id": {"$in": section.get("subSection", [])}})
        await db.sections.delete_one({"_id": section_id})

    await db.courses.delete_one({"_id": course["_id"]})

    return {"success": True, "message": "Course deleted successfully"}


@router.post("/createCategory")
async def create_category(
    payload: CreateCategoryRequest,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Admin")),
    db=Depends(get_db),
):
    if not payload.name:
        raise HTTPException(status_code=400, detail="All fields are required")

    await db.categories.insert_one({"name": payload.name, "description": payload.description, "courses": []})

    return {"success": True, "message": "Categorys Created Successfully"}


@router.get("/showAllCategories")
async def show_all_categories(db=Depends(get_db)):
    all_categories = await db.categories.find().to_list(length=None)
    return {"success": True, "data": _stringify_list(all_categories)}


@router.post("/getCategoryPageDetails")
async def category_page_details(payload: CategoryPageDetailsRequest, db=Depends(get_db)):
    selected_category = await db.categories.find_one({"_id": _oid(payload.categoryId)})
    if not selected_category:
        raise HTTPException(status_code=404, detail="Category not found")

    selected_courses = await db.courses.find(
        {"_id": {"$in": selected_category.get("courses", [])}, "status": "Published"}
    ).to_list(length=None)
    if not selected_courses:
        raise HTTPException(status_code=404, detail="No courses found for the selected category.")

    selected_category["courses"] = _stringify_list(selected_courses)

    categories_except = await db.categories.find({"_id": {"$ne": _oid(payload.categoryId)}}).to_list(length=None)
    different_category = None
    if categories_except:
        different_category = categories_except[0]
        different_courses = await db.courses.find(
            {"_id": {"$in": different_category.get("courses", [])}, "status": "Published"}
        ).to_list(length=None)
        different_category["courses"] = _stringify_list(different_courses)

    all_categories = await db.categories.find().to_list(length=None)
    all_courses = []
    for category in all_categories:
        courses = await db.courses.find(
            {"_id": {"$in": category.get("courses", [])}, "status": "Published"}
        ).to_list(length=None)
        all_courses.extend(courses)

    most_selling_courses = sorted(all_courses, key=lambda x: x.get("sold", 0), reverse=True)[:10]

    return {
        "success": True,
        "data": {
            "selectedCategory": with_string_id(selected_category),
            "differentCategory": with_string_id(different_category) if different_category else None,
            "mostSellingCourses": _stringify_list(most_selling_courses),
        },
    }


@router.post("/createRating")
async def create_rating(
    payload: CreateRatingRequest,
    user=Depends(get_current_user),
    _role=Depends(require_role("Student")),
    db=Depends(get_db),
):
    user_id = ObjectId(user["id"])
    course = await db.courses.find_one(
        {"_id": _oid(payload.courseId), "studentsEnroled": {"$elemMatch": {"$eq": user_id}}}
    )
    if not course:
        raise HTTPException(status_code=404, detail="Student is not enrolled in this course")

    already_reviewed = await db.ratingandreviews.find_one(
        {"user": user_id, "course": _oid(payload.courseId)}
    )
    if already_reviewed:
        raise HTTPException(status_code=403, detail="Course already reviewed by user")

    rating_review = {
        "rating": payload.rating,
        "review": payload.review,
        "course": _oid(payload.courseId),
        "user": user_id,
    }
    result = await db.ratingandreviews.insert_one(rating_review)

    await db.courses.update_one(
        {"_id": _oid(payload.courseId)}, {"$push": {"ratingAndReviews": result.inserted_id}}
    )

    return {
        "success": True,
        "message": "Rating and review created successfully",
        "ratingReview": with_string_id({**rating_review, "_id": result.inserted_id}),
    }


@router.get("/getAverageRating")
async def get_average_rating(courseId: str, db=Depends(get_db)):
    pipeline = [
        {"$match": {"course": _oid(courseId)}},
        {"$group": {"_id": None, "averageRating": {"$avg": "$rating"}}},
    ]
    result = await db.ratingandreviews.aggregate(pipeline).to_list(length=None)

    if result:
        return {"success": True, "averageRating": result[0]["averageRating"]}

    return {"success": True, "averageRating": 0}


@router.get("/getReviews")
async def get_all_rating_review(db=Depends(get_db)):
    all_reviews = await db.ratingandreviews.find().sort("rating", -1).to_list(length=None)

    for review in all_reviews:
        user_doc = await db.users.find_one({"_id": review.get("user")})
        if user_doc:
            review["user"] = {
                "firstName": user_doc.get("firstName"),
                "lastName": user_doc.get("lastName"),
                "email": user_doc.get("email"),
                "image": user_doc.get("image"),
            }
        course_doc = await db.courses.find_one({"_id": review.get("course")})
        if course_doc:
            review["course"] = {"courseName": course_doc.get("courseName")}

    return {"success": True, "data": _stringify_list(all_reviews)}


@router.post("/addSection")
async def create_section(
    payload: CreateSectionRequest,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    if not payload.sectionName or not payload.courseId:
        raise HTTPException(status_code=400, detail="Missing required properties")

    section_result = await db.sections.insert_one({"sectionName": payload.sectionName, "subSection": []})

    await db.courses.update_one(
        {"_id": _oid(payload.courseId)},
        {"$push": {"courseContent": section_result.inserted_id}},
    )

    updated_course = await _get_full_course(db, _oid(payload.courseId), include_video=True)

    return {
        "success": True,
        "message": "Section created successfully",
        "updatedCourse": updated_course,
    }


@router.post("/updateSection")
async def update_section(
    payload: UpdateSectionRequest,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    await db.sections.update_one(
        {"_id": _oid(payload.sectionId)}, {"$set": {"sectionName": payload.sectionName}}
    )

    course = await _get_full_course(db, _oid(payload.courseId), include_video=True)

    return {"success": True, "message": "Section updated", "data": course}


@router.post("/deleteSection")
async def delete_section(
    payload: DeleteSectionRequest,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    await db.courses.update_one(
        {"_id": _oid(payload.courseId)},
        {"$pull": {"courseContent": _oid(payload.sectionId)}},
    )

    section = await db.sections.find_one({"_id": _oid(payload.sectionId)})
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    await db.subsections.delete_many({"_id": {"$in": section.get("subSection", [])}})
    await db.sections.delete_one({"_id": _oid(payload.sectionId)})

    course = await _get_full_course(db, _oid(payload.courseId), include_video=True)

    return {"success": True, "message": "Section deleted", "data": course}


@router.post("/addSubSection")
async def create_subsection(
    sectionId: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    video: UploadFile = File(...),
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    if not sectionId or not title or not description or not video:
        raise HTTPException(status_code=404, detail="All Fields are Required")

    upload_details = upload_image_to_cloudinary(video, settings.cloud_folder)

    sub_section = {
        "title": title,
        "timeDuration": str(upload_details.get("duration", 0)),
        "description": description,
        "videoUrl": upload_details.get("secure_url"),
    }
    sub_result = await db.subsections.insert_one(sub_section)

    await db.sections.update_one(
        {"_id": _oid(sectionId)}, {"$push": {"subSection": sub_result.inserted_id}}
    )
    updated_section = await db.sections.find_one({"_id": _oid(sectionId)})
    if updated_section:
        subsections = await db.subsections.find({"_id": {"$in": updated_section.get("subSection", [])}}).to_list(length=None)
        updated_section["subSection"] = _stringify_list(subsections)

    return {"success": True, "data": with_string_id(updated_section)}


@router.post("/updateSubSection")
async def update_subsection(
    payload: UpdateSubSectionRequest,
    request: Request,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    sub_section = await db.subsections.find_one({"_id": _oid(payload.subSectionId)})
    if not sub_section:
        raise HTTPException(status_code=404, detail="SubSection not found")

    updates: dict[str, Any] = {}
    if payload.title is not None:
        updates["title"] = payload.title
    if payload.description is not None:
        updates["description"] = payload.description

    form = await request.form()
    video = form.get("video") if form else None
    if video is not None and hasattr(video, "filename"):
        upload_details = upload_image_to_cloudinary(video, settings.cloud_folder)
        updates["videoUrl"] = upload_details.get("secure_url")
        updates["timeDuration"] = str(upload_details.get("duration", 0))

    if updates:
        await db.subsections.update_one({"_id": _oid(payload.subSectionId)}, {"$set": updates})

    updated_section = await db.sections.find_one({"_id": _oid(payload.sectionId)})
    if updated_section:
        subsections = await db.subsections.find({"_id": {"$in": updated_section.get("subSection", [])}}).to_list(length=None)
        updated_section["subSection"] = _stringify_list(subsections)

    return {
        "success": True,
        "message": "Section updated successfully",
        "data": with_string_id(updated_section),
    }


@router.post("/deleteSubSection")
async def delete_subsection(
    payload: DeleteSubSectionRequest,
    _user=Depends(get_current_user),
    _role=Depends(require_role("Instructor")),
    db=Depends(get_db),
):
    await db.sections.update_one(
        {"_id": _oid(payload.sectionId)},
        {"$pull": {"subSection": _oid(payload.subSectionId)}},
    )

    sub_section = await db.subsections.find_one_and_delete({"_id": _oid(payload.subSectionId)})
    if not sub_section:
        raise HTTPException(status_code=404, detail="SubSection not found")

    updated_section = await db.sections.find_one({"_id": _oid(payload.sectionId)})
    if updated_section:
        subsections = await db.subsections.find({"_id": {"$in": updated_section.get("subSection", [])}}).to_list(length=None)
        updated_section["subSection"] = _stringify_list(subsections)

    return {
        "success": True,
        "message": "SubSection deleted successfully",
        "data": with_string_id(updated_section),
    }


@router.post("/updateCourseProgress")
async def update_course_progress(
    payload: UpdateCourseProgressRequest,
    user=Depends(get_current_user),
    _role=Depends(require_role("Student")),
    db=Depends(get_db),
):
    subsection = await db.subsections.find_one({"_id": _oid(payload.subsectionId)})
    if not subsection:
        raise HTTPException(status_code=404, detail="Invalid subsection")

    course_progress = await db.courseprogresses.find_one(
        {"courseID": _oid(payload.courseId), "userId": ObjectId(user["id"])}
    )

    if not course_progress:
        raise HTTPException(status_code=404, detail="Course progress Does Not Exist")

    if payload.subsectionId in [str(x) for x in course_progress.get("completedVideos", [])]:
        raise HTTPException(status_code=400, detail="Subsection already completed")

    await db.courseprogresses.update_one(
        {"_id": course_progress["_id"]},
        {"$push": {"completedVideos": _oid(payload.subsectionId)}},
    )

    return {"message": "Course progress updated"}


async def _get_full_course(db, course_id: ObjectId, include_video: bool) -> dict | None:
    course_details = await db.courses.find_one({"_id": course_id})
    if not course_details:
        return None

    instructor = await db.users.find_one({"_id": course_details.get("instructor")})
    if instructor:
        profile_id = instructor.get("additionalDetails")
        if profile_id:
            profile = await db.profiles.find_one({"_id": profile_id})
            instructor["additionalDetails"] = with_string_id(profile)
        course_details["instructor"] = with_string_id(instructor)

    category = await db.categories.find_one({"_id": course_details.get("category")})
    if category:
        course_details["category"] = with_string_id(category)

    rating_ids = course_details.get("ratingAndReviews", [])
    if rating_ids:
        ratings = await db.ratingandreviews.find({"_id": {"$in": rating_ids}}).to_list(length=None)
        course_details["ratingAndReviews"] = _stringify_list(ratings)

    populated_sections = []
    for section_id in course_details.get("courseContent", []):
        section = await db.sections.find_one({"_id": section_id})
        if not section:
            continue
        subsections = await db.subsections.find({"_id": {"$in": section.get("subSection", [])}}).to_list(length=None)
        if not include_video:
            for sub in subsections:
                sub.pop("videoUrl", None)
        section["subSection"] = _stringify_list(subsections)
        populated_sections.append(with_string_id(section))

    course_details["courseContent"] = populated_sections

    return with_string_id(course_details)
