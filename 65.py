# 65. Multiplication table of a given number
num = int(input("Enter number: "))
n = int(input("Enter table size (e.g., 10): "))

for i in range(1, n+1):
    print(f"{num} x {i} = {num*i}")
