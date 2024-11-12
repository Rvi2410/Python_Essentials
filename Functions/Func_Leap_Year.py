def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return False
    elif year % 400 != 0:
        return False
    else:
        return True


##########################
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    year = test_data[i]
    print(year,"-> ",end="")
    result = is_year_leap(year)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
