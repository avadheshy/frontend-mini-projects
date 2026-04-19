from pydantic import BaseModel


class UpdateProfileRequest(BaseModel):
    firstName: str | None = ""
    lastName: str | None = ""
    dateOfBirth: str | None = ""
    about: str | None = ""
    contactNumber: str | None = ""
    gender: str | None = ""
