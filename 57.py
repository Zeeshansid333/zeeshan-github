# 57. Print all prime numbers from 1 to N
n = int(input("Enter N: "))
def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(2, n+1):
    if is_prime(i):
        print(i, end=" ")
