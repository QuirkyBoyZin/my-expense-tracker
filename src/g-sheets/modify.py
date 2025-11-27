import os
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service_account_file = "Credential.json"
creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
sheet_id = "1VhkGo_GYGfHyWWM0Mt6Yr_UsJ-tE0wkTllxwFvhFL7M"
client = gspread.authorize(creds)
SHEET_GID = 0  # change if your tab has a different gid
DATA_RANGE = "A2:F"
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
workbook = client.open_by_key(sheet_id)
sheet_gspread = workbook.worksheet("expense_tracker")


def add_row (type,name,price):
    print("In progress...")
    data = sheet_gspread.get_all_records()
    id=len(data)+1
    item=[id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]
    new=sheet_gspread.append_row(item)
    print("Done")
    return new
    
def remove_row(L):
    updated_data = sheet_gspread.get_all_records()
    row_index = None
    for i, row in enumerate(updated_data, start=2):
        if str(row["ID"]) == str(L):
            row_index = i
            break
    if row_index == None:
        return "ID is not found"
    sheet_gspread.delete_rows(row_index)

    updated_data = sheet_gspread.get_all_records()
    for new_id, row in enumerate(updated_data, start=1):
        sheet_gspread.update_cell(new_id + 1, 1, new_id)
    

def update_row(row_id, type, name, price):
    data = sheet_gspread.get_all_records()

    row_index = None
    for i, row in enumerate(data, start=2):
        if str(row["ID"]) == str(row_id):
            row_index = i
            break

    if row_index is None:
        return None

    new_row = [row_id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]

    sheet_gspread.update(f"A{row_index}:F{row_index}", [new_row])
    return new_row


    
# print(update_row_in_sheet(L))
# remove_sheet(i)
add_row("drink","coca","free")
# print(update_row(2,"food","pizza","91"))





