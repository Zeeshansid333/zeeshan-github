n = int(input("Enter a three-digit number: "))

if 100 <= n <= 999:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    total = a ** 3 + b ** 3 + c ** 3

    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Please enter a three-digit number")
