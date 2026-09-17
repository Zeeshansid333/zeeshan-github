# 71. Convert decimal to binary
n = int(input("Enter decimal number: "))
if n == 0:
    print(0)
else:
    bin_str = ""
    x = n
    sign = ""
    if x < 0:
        sign = "-"
        x = -x
    while x > 0:
        bin_str = str(x % 2) + bin_str
        x //= 2
    print(sign + bin_str)
