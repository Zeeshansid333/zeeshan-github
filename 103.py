# 103 (clean standard butterfly for n rows)
n = int(input("Enter n: "))

for i in range(n):
    left = "*"*(i+1)
    right = "*"*(i+1)
    middle_spaces = " "*(2*(n-i)-3)
    if middle_spaces == "":
        print(left + right)
    else:
        if i == n-1:
            print("*"*(2*n-1))
        else:
            print(left + " "*(2*(n-i)-3) + right)
for i in range(n-2, -1, -1):
    left = "*"*(i+1)
    right = "*"*(i+1)
    middle_spaces = " "*(2*(n-i)-3)
    if i == 0:
        print("*" + " "*(2*n-3) + "*")
    else:
        if middle_spaces == "":
            print(left + right)
        else:
            print(left + " "*(2*(n-i)-3) + right)
