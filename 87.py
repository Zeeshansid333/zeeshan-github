# 87. Sandglass / Hourglass
n = int(input("Enter n: "))  # top size (rows)
# top
for i in range(n, 0, -1):
    print("*"*(2*i-1))
# middle gap is already handled by printing bottom part
for i in range(2, n+1):
    print("*"*(2*i-1))
