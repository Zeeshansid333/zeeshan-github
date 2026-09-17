# 106. Zigzag pattern (stars) as sample:
# * * * *
#    *
# * * * *
n = int(input("Enter n columns on first row (even recommended): "))
# We'll use rows=3 as in sample: first row, middle row, last row
for i in range(2):
    print("* "*(n//2)).rstrip()
print(" "*(n-1) + "*")
