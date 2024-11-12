# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

Year = int(input("Enter a Year : "))

if Year < 1582:
    print(Year, "is nornal year")
else:
    if Year % 4 == 0:
#    print(Year, "is normal Year")
        if Year % 100 == 0:
#        print(Year, "is normal Year")
            if Year % 400 == 0:
                print(Year, "is leap year")
            else:
                print(Year, "is Normal Year")

