# 94. Inverted number triangle
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n = int(input("Enter rows: "))
for i in range(n, 0, -1):
    print(" ".join(str(x) for x in range(1, i+1)))
