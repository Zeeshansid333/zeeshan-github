# 61. Sum: 1 + 1/2 + ... + 1/N
n = int(input("Enter N: "))
s = 0.0
for i in range(1, n+1):
    s += 1.0/i
print(s)
