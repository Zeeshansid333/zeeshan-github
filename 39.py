hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours < 0 or rate < 0:
    print("Invalid input")
elif hours <= 40:
    salary = hours * rate
    print("Salary:", salary)
else:
    regular_salary = 40 * rate
    overtime_hours = hours - 40
    overtime_salary = overtime_hours * rate * 1.5

    salary = regular_salary + overtime_salary
    print("Regular salary:", regular_salary)
    print("Overtime salary:", overtime_salary)
    print("Total salary:", salary)
