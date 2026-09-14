# 6. Greater of two numbers
a, b = map(float, input("Enter two numbers: ").split())

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")
