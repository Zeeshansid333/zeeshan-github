# 70. Perfect number check: sum of proper divisors == number
n = int(input("Enter number: "))
if n <= 1:
    print("Not Perfect")
else:
    s = 1  # 1 is a proper divisor for n>1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
    print("Perfect" if s == n else "Not Perfect")
