# 97. Binary number triangle
# 0
# 0 1
# 0 1 0
# 0 1 0 1
n = int(input("Enter rows: "))
for i in range(1, n+1):
    row = []
    for j in range(i):
        row.append(str(j % 2))
    print(" ".join(row))
