import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        raw_password = os.getenv("app_password", "abcd efgh ijkl mnop")
        self.app_password = raw_password.replace(" ", "").strip().strip('"').strip("'")
        self.email_address = {placeholder_sender_email}
        self.reciever_email = {placeholder_reciever_email}  
        self.attachments = [
            r"docs\passport.pdf",
            r"docs\acceptance.pdf",
        ]
        self.subject = {passport_number_placeholder}
        
