import sheets 
from datetime import datetime

def add_row (type,name,price):
    print("In progress...")
    data = sheets.sheet_gspread.get_all_records()
    id=len(data)+1
    item=[id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]
    new=sheets.sheet_gspread.append_row(item)
    print("Done")
    return new
    
def remove_row(L):
    updated_data = sheets.sheet_gspread.get_all_records()
    row_index = None
    for i, row in enumerate(updated_data, start=2):
        if str(row["ID"]) == str(L):
            row_index = i
            break
    if row_index == None:
        return "ID is not found"
    sheets.sheet_gspread.delete_rows(row_index)

    updated_data = sheets.sheet_gspread.get_all_records()
    for new_id, row in enumerate(updated_data, start=1):
        sheets.sheet_gspread.update_cell(new_id + 1, 1, new_id)
    

def update_row(row_id, type, name, price):
    data = sheets.sheet_gspread.get_all_records()

    row_index = None
    for i, row in enumerate(data, start=2):
        if str(row["ID"]) == str(row_id):
            row_index = i
            break

    if row_index is None:
        return None

    new_row = [row_id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]

    sheets.sheet_gspread.update(f"A{row_index}:F{row_index}", [new_row])
    return new_row

if __name__ == "__main__":
   pass


    


