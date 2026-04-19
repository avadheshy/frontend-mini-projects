from fastapi import APIRouter

from app.api.v1.endpoints import auth, profile, course, payment, contact

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(course.router, prefix="/course", tags=["course"])
api_router.include_router(payment.router, prefix="/payment", tags=["payment"])
api_router.include_router(contact.router, prefix="/reach", tags=["contact"])
