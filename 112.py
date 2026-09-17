# 112. Square with diagonals marked
n = int(input("Enter size n (>=2): "))
for i in range(n):
    row = []
    for j in range(n):
        if i == j or j == n-1-i:
            row.append("*")
        else:
            row.append(" ")
    print(" ".join(row))
