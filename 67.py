# 67. Armstrong number (generalized for any digits)
n = int(input("Enter number: "))
temp = abs(n)
digits = 0
if temp == 0:
    digits = 1
else:
    while temp > 0:
        digits += 1
        temp //= 10

temp = abs(n)
sum_ = 0
while temp > 0:
    d = temp % 10
    sum_ += d ** digits
    temp //= 10

print("Armstrong" if sum_ == abs(n) else "Not Armstrong")
