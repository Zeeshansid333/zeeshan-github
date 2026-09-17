# 88. Number triangle (row-wise) as in sample:
# 1
# 22
# 33 3
# 4 4 4 4
# We'll print row i repeated i times with digit i.
n = int(input("Enter rows: "))
for i in range(1, n+1):
    print(str(i)*i)
