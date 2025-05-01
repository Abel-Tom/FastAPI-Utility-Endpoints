import smtplib
from email.message import EmailMessage
from threading import Thread
from core import config

def send_email_background(to_email: str, subject: str, body: str):
    def send():
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = config.EMAIL_USERNAME
            msg["To"] = to_email
            msg.set_content(body)

            with smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT) as server:
                server.starttls()
                server.login(config.EMAIL_USERNAME, config.EMAIL_PASSWORD)
                server.send_message(msg)

            print(f"✅ Email sent to {to_email}")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

    Thread(target=send).start()
