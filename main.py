import os.path
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from College import College

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1pwL5uqFL5t8QYTpBmDcitmmjZHeRfv93zh3PECebnV4'
START_CELL = "A10"  # Chabot College
END_CELL = "J19"  # LosMedanos College
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

        if not college_data:
            print('No data found.')
            return

        # Main code here
        generateLaTexCommandsFiles(college_data)

    except HttpError as err:
        print(err)


def generateLaTexCommandsFiles(college_data: List[str]):
    # 1. Create dictionary of College objects
    college_dict = createCollegeDictHelper(college_data)

    # 2. Write latex commands for each college
    for _, college in college_dict.items():
        createLaTexFile(college)


# Helper function to convert college spreadsheet into a map of College objects.
def createCollegeDictHelper(college_data: List[str]) -> dict:
    d = {}

    # 1. Loop through colleges
    for college in college_data:
        college_name = college[0]

        # First time seeing this college, initalize it
        if college_name not in d:
            d[college_name] = College()

        # 2. Add courses to College
        d[college_name].name = college[0]
        d[college_name].calcI.append(college[1])
        d[college_name].calcII.append(college[2])
        d[college_name].linearAlgebra.append(college[3])
        d[college_name].physics.append(college[4])
        d[college_name].csI.append(college[5])
        d[college_name].csII.append(college[6])
        d[college_name].discreteMathOrStructure.append(college[7])
        d[college_name].assemblyAndComputerArchitecture.append(college[7])

    return d

# Create LaTex command for college.
# TODO: Deal with multiple courses
def createLaTexFile(college: College) -> None:
    course_name = ["collegeName", "calcI", "calcII", "linearAlgebra", "physics", "csI", "csII",
                   "discreteMathOrStructure", "assemblyAndComputerArchitecture"]

    with open(college.name + ".tex", 'w') as f:
        # Write latex commands to file: \newcommand{\course}{course}
        name_command = "\\newcommand" + "{\\" + course_name[0] + "}" + "{" + college.name + "}" + '\n'
        calcI_command = "\\newcommand" + "{\\" + course_name[1] + "}" + "{" + " or ".join(college.calcI) + "}" + '\n'
        calcII_command = "\\newcommand" + "{\\" + course_name[2] + "}" + "{" + " or ".join(college.calcII) + "}" + '\n'
        linearAlgebra_command = "\\newcommand" + "{\\" + course_name[3] + "}" + "{" + " or ".join(
            college.linearAlgebra) + "}" + '\n'
        physics_command = "\\newcommand" + "{\\" + course_name[4] + "}" + "{" + " or ".join(
            college.physics) + "}" + '\n'
        csI_command = "\\newcommand" + "{\\" + course_name[5] + "}" + "{" + " or ".join(college.csI) + "}" + '\n'
        csII_command = "\\newcommand" + "{\\" + course_name[6] + "}" + "{" + " or ".join(college.csII) + "}" + '\n'
        discrete_command = "\\newcommand" + "{\\" + course_name[7] + "}" + "{" + " or ".join(
            college.discreteMathOrStructure) + "}" + '\n'
        assembly_command = "\\newcommand" + "{\\" + course_name[8] + "}" + "{" + " or ".join(
            college.assemblyAndComputerArchitecture) + "}" + '\n'

        f.write(name_command)
        f.write(calcI_command)
        f.write(calcII_command)
        f.write(linearAlgebra_command)
        f.write(physics_command)
        f.write(csI_command)
        f.write(csII_command)
        f.write(discrete_command)
        f.write(assembly_command)

    # Close file
    f.close()


if __name__ == '__main__':
    main()
