import math
import string

# 1. Arithmetic operations
a, b = map(float, input("Enter two numbers: ").split())

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
    print("Remainder:", a % b)
else:
    print("Quotient: Undefined")
    print("Remainder: Undefined")
