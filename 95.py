# 95. Column-wise incrementing
# 1
# 1 2
# 1 2 3
# 1 2 3 4
n = int(input("Enter rows: "))
for i in range(1, n+1):
    print(" ".join(str(x) for x in range(1, i+1)))
