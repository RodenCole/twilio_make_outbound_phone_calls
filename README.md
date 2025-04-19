# Twilio Voice Scheduler

A Python application that uses Twilio's Programmable Voice API to make automated outbound phone calls with scheduled appointments.

## Features

- Makes automated phone calls using Twilio's Voice API
- Reads out a personalized schedule for the recipient
- Uses TwiML (Twilio Markup Language) for voice instructions
- Configurable through environment variables

## Prerequisites

- Python 3.7 or higher
- Git
- Twilio account (https://www.twilio.com)
- Twilio phone number (for making calls)

## Security Best Practices

1. Never commit your `.env` file with actual credentials to version control
2. Use environment variables for all sensitive information
3. Keep your Twilio Account SID and Auth Token secure
4. Regularly rotate your Twilio credentials
5. Use a dedicated Twilio number for this application

## Setup Instructions

1. Clone the repository:
```bash
git clone [repository-url]
cd twilio_voice
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install twilio python-dotenv
```

4. Copy the example .env file and configure it:
```bash
cp .env.example .env
```

Edit the `.env` file with your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=recipient_phone_number
```

## Running the Application

1. Ensure your virtual environment is activated:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the script:
```bash
python make_call.py
```

## Project Structure

- `make_call.py`: Main Python script that makes the outbound call
- `.env.example`: Template for environment variables
- `.gitignore`: Git ignore file to prevent sensitive information from being committed
- `README.md`: This documentation file

## How it Works

The application uses Twilio's Voice API to make an outbound call to a specified recipient number. When the recipient answers, it reads out a personalized schedule using Twilio's text-to-speech capabilities. The schedule is formatted in TwiML, which controls how the voice message is delivered, including pauses between items for better clarity.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
