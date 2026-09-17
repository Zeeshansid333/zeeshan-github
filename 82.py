# 82. Pyramid (centered)
n = int(input("Enter n: "))  # rows
for i in range(1, n+1):
    stars = 2*i - 1
    print(" "*(n-i) + "*"*stars)
