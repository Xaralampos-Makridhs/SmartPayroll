import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

class EmailService:
    def __init__(self):
        self.sender_email = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASS")
        self.smtp_server = "smtp.gmail.com"
        self.port = 587

    def send_payslip(self, recipient_email, subject, body_text):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body_text, "plain"))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(message)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
