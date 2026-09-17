# 104. Hollow diamond inside rectangle (common)
n = int(input("Enter n (half height): "))
# rectangle height = 2n
for i in range(2*n):
    # i from 0..2n-1
    # diamond boundaries
    top = i
    bottom = 2*n - 1 - i
    dist = min(top, bottom)
    width = 2*n-1 - (2*dist)
    # left/right stars at extremes of rectangle
    # We'll implement rectangle with hollow diamond middle.
    # Outer rectangle:
    row = ["*"]*(2*n-1)
    # diamond "hole" edges:
    for j in range(1, 2*n-2):
        # diamond equation centered at n-1
        if abs(j-(n-1)) < (n-1-dist) and dist != n-1:
            row[j] = " "
    print(" ".join(row))
