# 101. Right-aligned alphabet triangle
n = int(input("Enter rows: "))
for i in range(1, n+1):
    row = [chr(ord('A') + j) for j in range(i)]
    print(" "*(n-i) + " ".join(row))
