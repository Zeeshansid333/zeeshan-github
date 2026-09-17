# 90. Floyd's triangle
n = int(input("Enter rows: "))
cur = 1
for i in range(1, n+1):
    row = []
    for _ in range(i):
        row.append(str(cur))
        cur += 1
    print(" ".join(row))
