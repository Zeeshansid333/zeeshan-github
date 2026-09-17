marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance")
elif marks >= 85 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

    if marks < 85:
        print("Marks requirement not satisfied")
    if attendance < 75:
        print("Attendance requirement not satisfied")
    if income > 250000:
        print("Family income requirement not satisfied")
