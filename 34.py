import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation")

else:
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print("Two real and distinct roots")
        print("Root 1:", root1)
        print("Root 2:", root2)

    elif discriminant == 0:
        root = -b / (2 * a)

        print("Two real and equal roots")
        print("Root:", root)

    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / abs(2 * a)

        print("Imaginary roots")
        print("Root 1:", real_part, "+", imaginary_part, "i")
        print("Root 2:", real_part, "-", imaginary_part, "i")
