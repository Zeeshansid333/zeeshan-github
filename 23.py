hour = int(input("Enter hour in 24-hour format: "))

if hour < 0 or hour > 23:
    print("Invalid hour")
elif hour < 12:
    print("Morning")
elif hour < 17:
    print("Afternoon")
elif hour < 21:
    print("Evening")
else:
    print("Night")
