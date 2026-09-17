# 93. Number pyramid (centered) with increasing lengths as sample:
# row1: 1
# row2: 1 2 3
# row3: 1 2 3 4 5
n = int(input("Enter rows: "))
for i in range(1, n+1):
    start = 1
    end = 2*i - 1
    print(" "*(n-i), end="")
    print(" ".join(str(x) for x in range(start, end+1)))
