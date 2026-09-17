# 51. Palindrome check (number)
n = int(input("Enter number: "))
orig = n
n = abs(n)

rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

# Handle negative as not palindrome
if orig < 0:
    print("Not Palindrome")
else:
    print("Palindrome" if rev == orig else "Not Palindrome")
