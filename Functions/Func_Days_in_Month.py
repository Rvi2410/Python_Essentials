def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return False
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = days[month -1]
    if month == 2 and is_year_leap(year):
        day = 29
    return day

def day_of_year(year):
    if year == is_year_leap(year):
        return true

print(day_of_year(2000))

