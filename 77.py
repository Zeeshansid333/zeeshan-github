# 77. Increasing + Decreasing using one recursive function
def inc_dec(n, i=1, direction=1):
    # direction=1 for increasing, -1 for decreasing
    if direction == 1:
        if i > n:
            return inc_dec(n, n-1, -1)
        print(i, end=" ")
        return inc_dec(n, i+1, 1)
    else:
        if i < 1:
            return
        print(i, end=" ")
        return inc_dec(n, i-1, -1)

n = int(input("Enter N: "))
inc_dec(n)
