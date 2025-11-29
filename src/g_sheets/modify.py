from datetime import datetime

def add_row (type,name,price,sheet):
    print("In progress...")
    data = sheet.get_all_records()
    id=len(data)+1
    item=[id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]
    new=sheet.append_row(item)
    print("Done")
    return new
    
def remove_row(L,sheet):
    updated_data = sheet.get_all_records()
    row_index = None
    for i, row in enumerate(updated_data, start=2):
        if str(row["ID"]) == str(L):
            row_index = i
            break
    if row_index == None:
        return "ID is not found"
    sheet.delete_rows(row_index)

    updated_data = sheet.get_all_records()
    for new_id, row in enumerate(updated_data, start=1):
        sheet.update_cell(new_id + 1, 1, new_id)
    

def update_row(row_id, type, name, price, sheet):
    data = sheet.get_all_records()

    row_index = None
    for i, row in enumerate(data, start=2):
        if str(row["ID"]) == str(row_id):
            row_index = i
            break

    if row_index is None:
        return None

    new_row = [row_id,datetime.now().strftime("%Y-%m-%d"),datetime.now().strftime("%H:%M:%S"),type,name,price]

    sheet.update(f"A{row_index}:F{row_index}", [new_row])
    return new_row

if __name__ == "__main__":
   pass


    


