# 72. Convert binary to decimal
b = input("Enter binary: ").strip()
if not all(ch in "01" for ch in b):
    print("Invalid binary")
else:
    val = 0
    for ch in b:
        val = val*2 + int(ch)
    print(val)
