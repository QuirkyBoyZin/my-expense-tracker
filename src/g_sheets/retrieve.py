from . import sheets
from datetime import datetime, timedelta

def retrieve_items() -> list:
    result = sheets.sheet.values().get(spreadsheetId=sheets.sheet_id,range = sheets.DATA_RANGE).execute()
    return result.get("values", [])
def get_data(date: str):
    rows = retrieve_items()
    return [r for r in rows if len(r) > 1 and r[1] == date]
def data_range(start_date: str, end_date: str):
    s = datetime.strptime(start_date, "%Y-%m-%d")
    e = datetime.strptime(end_date, "%Y-%m-%d")
    while s <= e:
        yield s.strftime("%Y-%m-%d")
        s += timedelta(days=1)

def get_data_from(date1: str, date2: str):
    rows = retrieve_items()
    result = {}
    for d in data_range(date1, date2):
        filtered = [r for r in rows if len(r) > 1 and r[1] == d]
        if filtered:
            result[d] = filtered
    return result
def get_category(category):
    rows = retrieve_items()
    price = []
    for r in rows:
        if len(r) >= 6:
            if r[3].lower() == category.lower():
                try:
                    price.append(float(r[5]))
                except ValueError:
                    pass
    return price

def get_item(date_str, item_id):
    rows = get_data(date_str)   
    for r in rows:
        if r[0] == item_id:
            return [r[3], r[4], r[5]]
    return None

if __name__ == "__main__":
    pass