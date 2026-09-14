# 8. Check whether three numbers are equal
a, b, c = map(float, input("Enter three numbers: ").split())

if a == b and b == c:
    print("All three numbers are equal")
else:
    print("Numbers are not equal")
