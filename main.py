import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
import config

settings = config.Settings()

# ==========================================
# GMAIL CONFIGURATION
# ==========================================
GMAIL_EMAIL = settings.email_address
GMAIL_APP_PASSWORD = settings.app_password

TO_EMAIL = settings.reciever_email
SUBJECT = settings.subject
BODY = """
Full Name: Himma Gaji

Type of Visa: Long Term Visa

Purpose of stay: Study

Email address: wwnsmichael@gmail.com
"""

# List all files you want to attach
ATTACHMENTS = settings.attachments

# ==========================================
# CREATE EMAIL
# ==========================================

message = EmailMessage()
message["From"] = GMAIL_EMAIL
message["To"] = TO_EMAIL
message["Subject"] = SUBJECT
message.set_content(BODY)

# ==========================================
# ADD ATTACHMENTS
# ==========================================

for file in ATTACHMENTS:
    path = Path(file)

    if path.exists():
        with open(path, "rb") as f:
            message.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=path.name,
            )
    else:
        print(f"File not found: {path}")

# ==========================================
# SEND EMAIL
# ==========================================

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        smtp.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)