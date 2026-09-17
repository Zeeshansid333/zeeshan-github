# 49. Sum of digits
n = int(input("Enter number: "))
n = abs(n)
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)
