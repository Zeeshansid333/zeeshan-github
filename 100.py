# 100. Reverse alphabet triangle
# A B C D
# A B C
# A B
# A
n = int(input("Enter rows: "))
for i in range(n, 0, -1):
    row = [chr(ord('A') + j) for j in range(i)]
    print(" ".join(row))
