from sqlalchemy.orm import Session
from app.schemas.codeClient import CodeClientCreate
from app.models.codeClient import CodeClient

import os
from twilio.rest import Client
import random

def send_sms(to_number: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
    
    client = Client(account_sid, auth_token)
    presentCode = random.randint(100000, 999999)
    message = f"¡Gracias por tu preferencia! Canjea el siguiente código por un obsequio:{presentCode}"

    msg = client.messages.create(
        to=f"+52{to_number}",
        from_=twilio_number,
        body=message
    )
    return msg.sid, msg.status, presentCode

def save_code_client(db:Session, codeClient:CodeClientCreate):
    db_code = CodeClient(**codeClient.dict())
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code