# 19. Largest of three numbers
a, b, c = map(float, input("Enter three numbers: ").split())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
