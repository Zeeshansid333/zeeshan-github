# 92. Pascal's triangle
n = int(input("Enter rows: "))
for i in range(n):
    # spaces
    print(" "*(n-i-1), end="")
    # values
    c = 1
    for j in range(i+1):
        if j == 0:
            print(c)
        else:
            # compute next binomial coefficient
            c = c * (i - j + 1) // j
            print("   ", c, end="")
    # fix formatting by using a simple line rebuild instead
