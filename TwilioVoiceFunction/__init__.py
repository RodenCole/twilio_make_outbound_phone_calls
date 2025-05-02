import logging
import azure.functions as func
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Get Twilio credentials from environment variables
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        twilio_number = os.environ["TWILIO_PHONE_NUMBER"]
        
        # Get the recipient number from the request
        req_body = req.get_json()
        recipient_number = req_body.get('to_number')
        
        if not recipient_number:
            return func.HttpResponse(
                "Please provide a 'to_number' in the request body",
                status_code=400
            )

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Make the call
        call = client.calls.create(
            twiml="""<Response>
                <Pause length="1"/>
                <Say>Hi, this is Jairosoft AI.</Say> 
                <Pause length="1"/>
                <Say>I've got your schedule for today:</Say>
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
            to=recipient_number,
            from_=twilio_number
        )

        return func.HttpResponse(
            f"Call initiated successfully! Call SID: {call.sid}",
            status_code=200
        )
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            f"An error occurred: {str(e)}",
            status_code=500
        ) 