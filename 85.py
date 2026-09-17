# 85. Hollow rectangle with width w and height h
h = int(input("Enter height: "))
w = int(input("Enter width: "))  # total columns of '*'
for i in range(h):
    if i == 0 or i == h-1:
        print("* " * w)
    else:
        print("* " + "  "*(w-2) + "*")
