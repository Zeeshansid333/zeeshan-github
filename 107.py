# 107. Spiral number matrix 4x4
N = 4
mat = [[0]*N for _ in range(N)]
num = 1
top, left, bottom, right = 0, 0, N-1, N-1
while top <= bottom and left <= right:
    for j in range(left, right+1):
        mat[top][j] = num; num += 1
    top += 1
    for i in range(top, bottom+1):
        mat[i][right] = num; num += 1
    right -= 1
    if top <= bottom:
        for j in range(right, left-1, -1):
            mat[bottom][j] = num; num += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1):
            mat[i][left] = num; num += 1
        left += 1

for r in mat:
    print(" ".join(f"{x:2d}" for x in r))
