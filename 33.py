a, b, c = map(int, input("Enter three numbers: ").split())

if a <= b and b <= c:
    x, y, z = a, b, c
elif a <= c and c <= b:
    x, y, z = a, c, b
elif b <= a and a <= c:
    x, y, z = b, a, c
elif b <= c and c <= a:
    x, y, z = b, c, a
elif c <= a and a <= b:
    x, y, z = c, a, b
else:
    x, y, z = c, b, a

print("Ascending order:", x, y, z)
