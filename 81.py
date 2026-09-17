# 81. Inverted right-aligned triangle
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*" * i)
