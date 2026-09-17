# 74. Sum of series: x - x^3/3! + x^5/5! - x^7/7! + ...
# We'll compute up to k terms (user input terms)
import math
x = float(input("Enter x: "))
k = int(input("Enter number of terms: "))

s = 0.0
sign = 1
power = 1
for i in range(k):
    # term i uses odd power: 1,3,5,... and factorial: 1!,3!,5!...
    odd = 2*i + 1
    term = (x ** odd) / math.factorial(odd)
    s += sign * term
    sign *= -1
print(s)
