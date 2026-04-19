from pydantic import BaseModel


class CapturePaymentRequest(BaseModel):
    courses: list[str]


class VerifyPaymentRequest(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str
    courses: list[str]


class PaymentSuccessEmailRequest(BaseModel):
    orderId: str
    paymentId: str
    amount: int
