ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character")
elif ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
