# 64. Compute: 1! + 2! + ... + N!
n = int(input("Enter N: "))
fact = 1
s = 0
for i in range(1, n+1):
    fact *= i
    s += fact
print(s)
