# 83. Inverted pyramid
n = int(input("Enter n: "))  # rows
for i in range(n, 0, -1):
    stars = 2*i - 1
    print(" "*(n-i) + "*"*stars)
