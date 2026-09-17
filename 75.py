# 75. Palindrome check for string using recursion
def is_pal(s, i=0):
    j = len(s) - 1 - i
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_pal(s, i+1)

s = input("Enter string: ")
print("Palindrome" if is_pal(s) else "Not Palindrome")
