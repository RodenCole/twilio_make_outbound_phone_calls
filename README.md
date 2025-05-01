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

## Local Setup Instructions

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
pip install -r requirements.txt
```

4. Copy the example .env file and configure it:

```bash
cp .env.example .env
```

Edit the `.env` file with your Twilio credentials:

## Azure Deployment Instructions

This application can be deployed to Azure as a Function App:

### Option 1: Azure Portal Deployment

1. In the Azure Portal, create a new Function App:

   - Choose Python as the runtime stack
   - Select Python 3.11 as the version
   - Choose the region and hosting plan (Consumption plan is recommended for low-volume usage)

2. Once the Function App is created, go to "Configuration" under Settings and add the following Application Settings:

   - `TWILIO_ACCOUNT_SID` - Your Twilio Account SID
   - `TWILIO_AUTH_TOKEN` - Your Twilio Auth Token
   - `TWILIO_PHONE_NUMBER` - Your Twilio phone number in E.164 format (e.g., +1234567890)
   - `RECIPIENT_PHONE_NUMBER` - Default recipient's phone number (optional)

3. Deploy your code using:
   - Azure CLI
   - Azure Functions Core Tools
   - Visual Studio Code with Azure Functions extension

### Option 2: GitHub Actions CI/CD (Recommended)

1. Fork/clone this repository to your GitHub account

2. In the Azure Portal:

   - Create a Function App as described in Option 1
   - Go to Function App → Overview → Get Publish Profile → Download the publish profile

3. In your GitHub repository:

   - Go to Settings → Secrets and variables → Actions
   - Add a new repository secret named `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` with the content of the downloaded publish profile file

4. GitHub Actions will automatically deploy your application to Azure on each push to the main branch

### Option 3: Azure CLI Deployment

1. Install Azure CLI and log in:

```bash
az login
```

2. Create Function App resources:

```bash
az group create --name TwilioVoiceResourceGroup --location eastus
az storage account create --name twiliovoicestorage --location eastus --resource-group TwilioVoiceResourceGroup --sku Standard_LRS
az functionapp create --name twilio-voice-app --storage-account twiliovoicestorage --consumption-plan-location eastus --resource-group TwilioVoiceResourceGroup --runtime python --runtime-version 3.11 --functions-version 4
```

3. Configure application settings:

```bash
az functionapp config appsettings set --name twilio-voice-app --resource-group TwilioVoiceResourceGroup --settings "TWILIO_ACCOUNT_SID=your_sid" "TWILIO_AUTH_TOKEN=your_token" "TWILIO_PHONE_NUMBER=your_number" "RECIPIENT_PHONE_NUMBER=recipient_number"
```

4. Deploy the application:

```bash
func azure functionapp publish twilio-voice-app
```

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
