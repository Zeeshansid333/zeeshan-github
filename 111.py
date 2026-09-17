# 111. Heart shape pattern (simple outline)
# This prints a common heart made of '*'
n = int(input("Enter size: "))  # use 3,4,5...
for i in range(2*n):
    line = ""
    for j in range(2*n):
        # heart equation approximation
        x = j - n
        y = i - n
        if (x*x + y*y - n*n) <= 0 and y < n:
            line += "*"
        else:
            line += " "
    print(line.rstrip())
