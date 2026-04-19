import smtplib
from email.message import EmailMessage

from app.core.config import settings



def send_mail(email: str, title: str, body: str) -> None:
    print("➡️ Starting send_mail function")

    if not settings.mail_host or not settings.mail_user or not settings.mail_pass:
        print("Mail settings missing")
        raise RuntimeError("Mail settings are not configured")

    try:
        print("➡️ Creating email message")
        message = EmailMessage()
        message["From"] = f"Studynotion | CodeHelp <{settings.mail_user}>"
        message["To"] = email
        message["Subject"] = title
        message.set_content(body, subtype="html")
        with smtplib.SMTP(settings.mail_host, 587) as smtp:
            smtp.starttls()
            smtp.login(settings.mail_user, settings.mail_pass)
            smtp.send_message(message)

    except Exception as e:
        print("Error occurred:", str(e))
        raise