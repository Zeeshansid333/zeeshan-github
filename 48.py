# 48. Count number of digits in a number
n = int(input("Enter number: "))
n = abs(n)
if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print(count)
