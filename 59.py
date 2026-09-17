# 59. LCM of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a, b = map(int, input("Enter two numbers: ").split())
g = gcd(a, b)
print("LCM:", abs(a*b)//g if g != 0 else 0)
