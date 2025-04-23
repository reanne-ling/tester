import gspread
import os
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

# Connect to a Google Sheet and optionally a specific worksheet
def connect_to_google_sheet(sheet_name="EOC Personnel Log", worksheet_index=0):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Load service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)

    # Open the sheet and select the worksheet
    sheet = client.open(sheet_name)
    worksheet = sheet.get_worksheet(worksheet_index)  # default is first tab (index 0)
    return worksheet