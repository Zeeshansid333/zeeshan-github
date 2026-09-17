# 105. Number diamond
n = int(input("Enter half size: "))

for i in range(n):
    # increasing
    print(" "*(n-i-1) + " ".join(str(x) for x in list(range(1, i+2)) + list(range(i, 0, -1))))
for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + " ".join(str(x) for x in list(range(1, i+2)) + list(range(i, 0, -1))))
