## comment when testing

from . import modify 
from . import retrieve

## uncomment when testing

# import modify
# import retrieve

import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

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
sheet_gspread = workbook.worksheet("Sheet1")

# Modifying data: add, update, remove

def add_row(category: str, name: str, price: float):
    modify.add_row(sheet_gspread, category, name, price)

def remove_row():
    pass

def change_row():
    pass

# Retrieving data

def get_all_expenses() -> list:
    return retrieve.retrieve_items(sheet, sheet_id, DATA_RANGE)

def get_expenses_at(date: str) -> list: 
    return retrieve.get_data(date, sheet, sheet_id, DATA_RANGE)
    
    


if __name__ == "__main__":
    pass