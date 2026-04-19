from fastapi import APIRouter, Depends

from app.api.deps import get_db
from app.mail.templates.contact_form_res import contact_us_email
from app.schemas.contact import ContactRequest
from app.utils.mail_sender import send_mail

router = APIRouter()


@router.post("/contact")
async def contact_us(payload: ContactRequest, _db=Depends(get_db)):
    try:
        send_mail(
            payload.email,
            "Your Data send successfully",
            contact_us_email(
                payload.email,
                payload.firstname,
                payload.lastname,
                payload.message,
                payload.phoneNo,
                payload.countrycode,
            ),
        )
        return {"success": True, "message": "Email send successfully"}
    except Exception:
        return {"success": False, "message": "Something went wrong..."}
