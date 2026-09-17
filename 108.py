# 108. Right arrow pattern
n = int(input("Enter height (odd recommended, e.g., 5): "))
# Example-like for n=5:
# *
# **
# ** *
# ** * *
# ** *
# **
# *
# We'll build based on rows=2n-1 where:
rows = 2*n-1
for i in range(rows):
    stars = min(i+1, rows-i)
    # add leading '**' and varying spaces then '*'
    if i < n:
        print("*"*2 + " "*(i-1) + ("*" if i>0 else ""))
    else:
        k = rows-i
        print("*"*2 + " "*(k-1) + ("*" if k>0 else ""))
