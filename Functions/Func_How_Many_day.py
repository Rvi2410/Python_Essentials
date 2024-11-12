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
    month1 = [1, 3, 5, 7, 8, 10, 12]
    month2 = [4, 6, 9, 11]
    month3 = [2]
    if year < 1582 or month < 1 or month > 12:
        return None
    for i in month1:
        if i == month:
            return 31
    for i in month2:
        if i == month:
            return 30
    for i in month3:
        if i == month:
            return 29
        else:
            return 28

def days_in_month1(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = days[month -1]
    if month == 2 and is_year_leap(year):
        day = 29
    return day



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    year = test_years[i]
    month = test_months[i]
    print(year, month, "->", end="")
    result = days_in_month1(year, month)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
