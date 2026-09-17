# 109. X pattern
n = int(input("Enter n rows/cols: "))
for i in range(n):
    row = []
    for j in range(n):
        row.append("*" if i == j or j == n-1-i else " ")
    print("".join(row))
