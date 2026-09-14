# 15. Count set bits
n = int(input("Enter a number: "))

count = 0
temp = n

while temp > 0:
    count += temp & 1
    temp >>= 1

print("Number of set bits:", count)
