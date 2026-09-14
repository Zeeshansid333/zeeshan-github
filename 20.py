# 20. Vowel or consonant
ch = input("Enter an alphabet: ").lower()

if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
