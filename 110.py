# 110. Plus (+) pattern
n = int(input("Enter n (size): "))

# plus arms length = n//2
mid = n//2
for i in range(n):
    row = ["*"]*n if False else [" "] * n
    for j in range(n):
        if j == mid or i == mid:
            row[j] = "*"
    print(" ".join(row))
