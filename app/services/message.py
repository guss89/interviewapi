import os
from twilio.rest import Client

def send_whatsapp_message(to_number: str, message: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("FROM_WHATSAPP")
    
    client = Client(account_sid, auth_token)

    msg = client.messages.create(
    from_=f"whatsapp:{from_whatsapp}",
    body=message,
    to=f"whatsapp:+521{to_number}"
    )
    return msg.sid, msg.status