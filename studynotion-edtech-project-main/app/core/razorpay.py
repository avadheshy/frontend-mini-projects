import razorpay

from app.core.config import settings


def get_razorpay_client() -> razorpay.Client:
    if not settings.razorpay_key or not settings.razorpay_secret:
        raise RuntimeError("Razorpay settings are not configured")
    return razorpay.Client(auth=(settings.razorpay_key, settings.razorpay_secret))
