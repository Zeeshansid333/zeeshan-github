x, y = map(float, input("Enter x and y coordinates: ").split())

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On the Y-axis")
elif y == 0:
    print("On the X-axis")
elif x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
else:
    print("Fourth quadrant")
