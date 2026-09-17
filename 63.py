# 63. Find x^n without using built-in pow
x = float(input("Enter x: "))
n = int(input("Enter n (non-negative): "))

if n < 0:
    print("Enter non-negative n")
else:
    ans = 1
    for _ in range(n):
        ans *= x
    print(ans)
