# 91. 1-0 alternating triangle
n = int(input("Enter rows: "))
for i in range(1, n+1):
    row = []
    for j in range(i):
        row.append(str((i+j) % 2))
    print(" ".join(row))
