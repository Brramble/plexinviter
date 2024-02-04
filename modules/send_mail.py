import smtplib
from email.mime.text import MIMEText
from config import SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_DISPLAYNAME, EMAIL_SUBJECT, EMAIL_MESSAGE

def send_email(user_email):
    try:
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            msg = MIMEText(EMAIL_MESSAGE)
            msg['Subject'] = EMAIL_SUBJECT
            #msg["From"] = EMAIL_SENDER
            msg["From"] = (f"{EMAIL_DISPLAYNAME} <{EMAIL_SENDER}>")
            msg['To'] = user_email

            server.sendmail(EMAIL_SENDER, [user_email], msg.as_string())
            print(f"Email sent successfully to {user_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
