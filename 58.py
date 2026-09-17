# 58. GCD / HCF of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a, b = map(int, input("Enter two numbers: ").split())
print(gcd(a, b))
