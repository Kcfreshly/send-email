import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        raw_password = os.getenv("app_password", "abcd efgh ijkl mnop")
        self.app_password = raw_password.replace(" ", "").strip().strip('"').strip("'")
        self.email_address = "wwnsmichael@gmail.com"
        self.reciever_email = "Abuja.Student.Visa@mzv.gov.cz"  
        #Abuja.Student.Visa@mzv.gov.cz
        self.attachments = [
            r"docs\passport.pdf",
            r"docs\acceptance.pdf",
        ]
        self.subject = "A12869455"
        
