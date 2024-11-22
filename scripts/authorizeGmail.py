from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Define the required Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authorize_gmail():
    creds = None
    # Try to load existing credentials from token.json
    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    except Exception as e:
        print("No valid token.json found. Generating a new one...")

    # If there are no valid credentials, start the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use the credentials.json file for the OAuth flow
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=3000)

        # Save the credentials to token.json
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    print("Authorization complete. Credentials saved to 'token.json'.")

if __name__ == '__main__':
    authorize_gmail()
