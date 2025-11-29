from models.expense import Expense
import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

import modify
import retrieve
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service_account_file = "credential.json"
creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
sheet_id = os.getenv("SHEET_ID")
client = gspread.authorize(creds)
SHEET_GID = 0  # change if your tab has a different gid
DATA_RANGE = "A2:F"
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
workbook = client.open_by_key(sheet_id)
sheet_gspread = workbook.worksheet("expense_tracker")
