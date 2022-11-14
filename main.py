import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from GUI import *

# Dropdown menu to pick school
# Generate pdf for each school, google folder, share folder
# Dont meet thanksgiving
# last week

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1pwL5uqFL5t8QYTpBmDcitmmjZHeRfv93zh3PECebnV4'
START_CELL = "A3"   # top left cell
END_CELL = "J37"    # bot right cell
RANGE_ID = f'Transfer Courses Table!{START_CELL}:{END_CELL}'


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API to retrieve college data from spreadsheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_ID
                                    ).execute()

        college_data = result.get('values', [])
        # print(college_data)
        if not college_data:
            print('No data found.')
            return

        # Start UI
        gui = GUI(college_data)

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
