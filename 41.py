hour, minute = map(int, input("Enter hour and minute: ").split())

if hour < 0 or hour > 12 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    hour = hour % 12

    hour_angle = hour * 30 + minute * 0.5
    minute_angle = minute * 6

    difference = abs(hour_angle - minute_angle)
    smaller_angle = min(difference, 360 - difference)

    print("Smaller angle:", smaller_angle, "degrees")
