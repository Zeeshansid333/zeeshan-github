# 52. Happy Number (reach 1 or not)
def is_happy(num):
    def next_num(x):
        s = 0
        while x > 0:
            d = x % 10
            s += d * d
            x //= 10
        return s

    slow = num
    fast = num
    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if slow == 1 or fast == 1:
            return True
        if slow == fast:
            return False

n = int(input("Enter number: "))
print("Happy" if is_happy(n) else "Not Happy")
