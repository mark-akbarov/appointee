from mailjet_rest import Client
from core.settings import MAILJET_API_KEY, MAILJET_SECRET_KEY


def send_email(recipient_email: str, code: str):
    api_key = MAILJET_API_KEY
    api_secret = MAILJET_SECRET_KEY
    mailjet = Client(auth=(api_key, api_secret), version='v3')
    data = {
    'FromEmail': "markakbarov@gmail.com",
    'FromName': "Your Verification Code",
    'Recipients': [
        {
        "Email": recipient_email,
        "Name": "Someone"
        }
    ],
    'Subject': "Verification Code",
    'Html-part': f"<h3>Dear User, welcome to this wonderful app!</h3><br />This is your verification code: <b>{code}</b>"
    }
    result = mailjet.send.create(data=data)
    if result.status_code == '200':
        return "success"