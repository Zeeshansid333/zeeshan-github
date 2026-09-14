# 14. Check whether the kth bit is set
n = int(input("Enter number: "))
k = int(input("Enter bit position, starting from 0: "))

if n & (1 << k):
    print("The kth bit is set")
else:
    print("The kth bit is not set")
