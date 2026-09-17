# 76. Count vowels in a string using recursion
def count_vowels(s, i=0):
    if i == len(s):
        return 0
    vowels = "aeiouAEIOU"
    return (1 if s[i] in vowels else 0) + count_vowels(s, i+1)

s = input("Enter string: ")
print("Vowel count:", count_vowels(s))
