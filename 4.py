# 4. Celsius and Fahrenheit conversion
choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter temperature: "))

if choice == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)
elif choice == "F":
    celsius = (temperature - 32) * 5 / 9
    print("Celsius:", celsius)
else:
    print("Invalid choice")
