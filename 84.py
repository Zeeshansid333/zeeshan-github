# 84. Diamond shape
n = int(input("Enter n: "))  # half size; diamond height = 2n-1
# upper
for i in range(1, n):
    print(" "*(n-i) + "*"*(2*i-1))
# lower (including middle width)
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
