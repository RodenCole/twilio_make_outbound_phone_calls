# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

# Test the call
call = client.calls.create(
    twiml="""<Response>
        <Pause length="1"/>
        <Say>Hi Aldred -- this is Jairosoft AI.</Say> 
        <Pause length="1"/>
        <Say>I've got your schedule for Sunday, April 20th, 2025:</Say>
        <Pause length="1"/>
        <Say>8:00 AM - 9:00 AM: Meeting with Miles</Say>
        <Pause length="1"/>
        <Say>9:00 AM - 10:00 AM: Meeting with Jayden</Say>
        <Pause length="1"/>
        <Say>11:00 AM - 12:00 PM: Lunch with Family</Say>
        <Pause length="1"/>
        <Say>1:00 PM - 5:00 PM: Meeting with Kriss</Say>
        <Pause length="1"/>
        <Say>Looks like a busy day!</Say>
        <Pause length="1"/>
        <Say>Is there anything else I can help you with regarding this schedule?</Say>
    </Response>""",
    to=os.environ["RECIPIENT_PHONE_NUMBER"],
    from_=os.environ["TWILIO_PHONE_NUMBER"],
)

print("Call initiated successfully!")
