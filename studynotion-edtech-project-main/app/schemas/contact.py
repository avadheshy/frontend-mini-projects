from pydantic import BaseModel, EmailStr


class ContactRequest(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    message: str
    phoneNo: str
    countrycode: str
