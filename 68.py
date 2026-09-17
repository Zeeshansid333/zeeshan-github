# 68. Largest and smallest digit in a number
n = input("Enter number: ").strip()
digits = [int(ch) for ch in n if ch.isdigit()]
if not digits:
    print("Invalid")
else:
    print("Largest digit:", max(digits))
    print("Smallest digit:", min(digits))
