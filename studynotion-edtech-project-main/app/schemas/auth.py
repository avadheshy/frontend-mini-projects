from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    confirmPassword: str
    accountType: str
    contactNumber: str | None = None
    otp: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SendOtpRequest(BaseModel):
    email: EmailStr


class ChangePasswordRequest(BaseModel):
    oldPassword: str
    newPassword: str


class ResetPasswordTokenRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    password: str
    confirmPassword: str
    token: str
