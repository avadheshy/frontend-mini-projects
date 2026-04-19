from pydantic import BaseModel


class CourseIdRequest(BaseModel):
    courseId: str


class CreateSectionRequest(BaseModel):
    sectionName: str
    courseId: str


class UpdateSectionRequest(BaseModel):
    sectionName: str
    sectionId: str
    courseId: str


class DeleteSectionRequest(BaseModel):
    sectionId: str
    courseId: str


class CreateSubSectionRequest(BaseModel):
    sectionId: str
    title: str
    description: str


class UpdateSubSectionRequest(BaseModel):
    sectionId: str
    subSectionId: str
    title: str | None = None
    description: str | None = None


class DeleteSubSectionRequest(BaseModel):
    subSectionId: str
    sectionId: str


class CreateCategoryRequest(BaseModel):
    name: str
    description: str | None = None


class CategoryPageDetailsRequest(BaseModel):
    categoryId: str


class CreateRatingRequest(BaseModel):
    rating: int
    review: str
    courseId: str


class UpdateCourseProgressRequest(BaseModel):
    courseId: str
    subsectionId: str
