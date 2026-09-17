# 99. Alphabet triangle (sequential)
# A
# A B
# A B C
# A B C D
n = int(input("Enter rows: "))
for i in range(1, n+1):
    row = [chr(ord('A') + j) for j in range(i)]
    print(" ".join(row))
