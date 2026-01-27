from emailservice.emailservice import EmailService

mailer = EmailService()

# Δοκιμαστική αποστολή στον εαυτό σου
success = mailer.send_payslip(
    recipient_email="makridhs.xaralampos@gmail.com",
    subject="Test Payslip",
    body_text="This is a test email from my Python app!"
)

if success:
    print("Το email στάλθηκε με επιτυχία!")