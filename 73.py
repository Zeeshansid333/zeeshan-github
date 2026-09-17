# 73. Read numbers until -1, print count and average
count = 0
total = 0
while True:
    x = int(input("Enter number (-1 to stop): "))
    if x == -1:
        break
    count += 1
    total += x

if count == 0:
    print("No numbers entered")
else:
    print("Count:", count)
    print("Average:", total / count)
