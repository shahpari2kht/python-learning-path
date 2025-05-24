from datetime import date, datetime

def calculate_age(birth_date):
    today = date.today()
    # محاسبه تفاوت سال‌ها
    age = today.year - birth_date.year
    # بررسی اینکه روز تولد گذشته یا نه
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

input_str = input().strip()
try:
    y, m, d = map(int, input_str.split("/"))
    if is_valid_date(y, m, d):
        print(calculate_age(date(y, m, d)))
    else:
        print("WRONG")
except:
    print("WRONG")
