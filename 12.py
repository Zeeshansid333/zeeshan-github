# 12. Swap two numbers using XOR
a, b = map(int, input("Enter two integers: ").split())

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
