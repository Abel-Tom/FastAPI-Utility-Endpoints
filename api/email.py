from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from utils.email_sender import send_email_background
from core import config

email_router = APIRouter()

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str

@email_router.post("/send-email")
def send_email(request: EmailRequest):
    send_email_background(request.to_email, request.subject, request.body)
    return {"message": "Email is being sent in the background."}

# @email_router.get("/test")
# def test_email():
#     return {"message": f'{config.EMAIL_USERNAME} {config.EMAIL_PASSWORD}'}
