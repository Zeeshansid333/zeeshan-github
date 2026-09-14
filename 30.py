a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

match operator:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b == 0:
            print("Division by zero is not allowed")
        else:
            print("Result:", a / b)
    case _:
        print("Invalid operator")
