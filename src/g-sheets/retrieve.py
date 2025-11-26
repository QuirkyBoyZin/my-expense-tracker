import sheets

def retrieve_items() -> list:
    result = sheets.sheet.values().get(spreadsheetId=sheets.sheet_id,range = sheets.DATA_RANGE).execute()
    return result.get("values", [])
def get_data(date: str):
    rows = retrieve_items()
    return [r for r in rows if len(r) > 1 and r[1] == date]
def data_range(start_row: int, end_row: int):
    s = sheets.datetime(start_row, "%Y-%m-%d" )
    e = sheets.datetime(end_row, "%Y-%m-%d" )
    while s <= e:
        yield s.strftime("%Y-%m-%d")
        s += sheets.timedelta(days=1)
def get_data_from(date1,date2):
    row = retrieve_items()
    result = []
    for d in data_range(date1,date2):
        filtered =[r for r in row if len(row) > 1 and r[1] == d]
        if filtered:
           result[d] = filtered 
    return result
def get_category(category):
    row = retrieve_items()
    price = []
    for r in row:
        if len(r) >= 6:
            if row[3].lower() == category.lower():
                try:
                    price.append(float(r[5]))
                except ValueError:
                    pass
    return price
def get_item(date_str, id):
    row = retrieve_items(date_str)
    for r in row:
        if row[0] == id:
            return [ r[3] , r[4], r[5]]
    return None
if __name__ == "__main__":
    date = input("Enter date (YYYY-MM-DD): ")   
    print(get_data(date))