# 102. Alphabet pyramid (centered)
# A
# B A B
# C B A B C ...
n = int(input("Enter rows: "))
for i in range(1, n+1):
    left = [chr(ord('A') + j) for j in range(i)]
    right = left[-2::-1]
    row = left + right
    print(" "*(n-i) + " ".join(row))
