import math

def show_menu():
    print("\n=== ADVANCED CALCULATOR ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Log (base 10)")
    print("11. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == '4':
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        if b == 0:
            print("Error: Division by zero!")
        else:
            print("Result:", a / b)

    elif choice == '5':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print("Result:", math.pow(base, exponent))

    elif choice == '6':
        num = float(input("Enter number: "))
        if num < 0:
            print("Error: Negative number for square root!")
        else:
            print("Result:", math.sqrt(num))

    elif choice == '7':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.sin(math.radians(angle)))

    elif choice == '8':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.cos(math.radians(angle)))

    elif choice == '9':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.tan(math.radians(angle)))

    elif choice == '10':
        num = float(input("Enter number: "))
        if num <= 0:
            print("Error: Log undefined for zero or negative!")
        else:
            print("Result:", math.log10(num))

    elif choice == '11' or choice.lower() == 'exit':
        print("Exiting calculator. Thank you!")
        break

    else:
        print("Invalid input! Please try again.")
