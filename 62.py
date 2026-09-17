# 62. 1 − 2 + 3 − 4 + ... up to N terms
n = int(input("Enter N: "))
s = 0
sign = 1
for i in range(1, n+1):
    s += sign * i
    sign *= -1
print(s)
