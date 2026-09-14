day = int(input("Enter day number 1-7: "))

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

if 1 <= day <= 7:
    print(days[day - 1])
else:
    print("Invalid day number")
