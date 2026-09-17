# 98. Alphabet triangle (row repeat) example:
# A
# B B
# C C C
# D D D D
n = int(input("Enter rows (max 26 letters): "))
for i in range(n):
    ch = chr(ord('A') + i)
    print((ch + " ")* (i+1)).rstrip()
