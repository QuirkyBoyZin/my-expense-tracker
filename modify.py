import os
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service_account_file = "Credential.json"
creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
SPREADSHEET_ID = "1VhkGo_GYGfHyWWM0Mt6Yr_UsJ-tE0wkTllxwFvhFL7M"
client = gspread.authorize(creds)
workbook = client.open_by_key(SPREADSHEET_ID)
sheet = workbook.worksheet("expense_tracker")
range = "A1:F"
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
range = "A1:F"
sheet_read = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()    
result = sheet_read.get('values', [])
for i in result:
    print(i)
