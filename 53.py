# 53. Product of Digits using recursion
def product_digits(n):
    n = abs(n)
    if n == 0:
        return 1  # common approach: product of digits (0 alone handled below)
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)

n = int(input("Enter number: "))
if n == 0:
    print(0)
else:
    print(product_digits(n))
