# 69. Print all factors/divisors of a number
n = int(input("Enter number: "))
print("Factors:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
