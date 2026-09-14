month = int(input("Enter month number: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid month")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")
