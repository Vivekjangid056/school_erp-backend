from twilio.rest import Client
from django.conf import settings

def send_sms(to_number, message_body):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        return True, message.sid
    except Exception as e:
        return False, str(e)