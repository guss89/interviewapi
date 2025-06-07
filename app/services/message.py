import os
from twilio.rest import Client
import random

def send_sms(to_number: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
    
    client = Client(account_sid, auth_token)
    presentCode = random.randint(100000, 999999)
    message = f"¡Gracias por tu preferencia! Codigo de regalo:{presentCode}"

    msg = client.messages.create(
        to=f"+52{to_number}",
        from_=twilio_number,
        body=message
    )
    return msg.sid, msg.status