# 96. Reverse number triangle
# 4 3 2 1
# 3 2 1
# 2 1
# 1
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(" ".join(str(x) for x in range(i, 0, -1)))
