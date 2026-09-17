# 54. Extract and print each digit left to right
n = input("Enter number: ")
for ch in n:
    if ch.isdigit() or (ch=='-' and len(n)>1):
        if ch != '-':
            print(ch, end=" ")
