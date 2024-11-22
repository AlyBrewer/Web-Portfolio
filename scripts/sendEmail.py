from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import base64

def sendEmail(name, sender_email, message):
    # Load credentials from token.json
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=creds)

    # Create formatted email message
    mime_message = MIMEText(message)
    mime_message['To'] = '21brewera@gmail.com'
    mime_message['From'] = sender_email
    mime_message['Subject'] = f"Contact Form Submission from {name}"

    # Encode message
    encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode('utf-8')
    create_message = {'raw': encoded_message}

    # Send email
    try:
        send_message = service.users().messages().send(userId='me', body=create_message).execute()
        print(f"Message sent: {send_message['id']}")
    except Exception as e:
        print(f"Failed to send email: {e}")
