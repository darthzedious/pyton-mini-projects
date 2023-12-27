def addition(a, b):
    return f"Result: {a + b}"


def subtraction(a, b):
    return f"Result: {a - b}"


def division(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return f"Result: {a / b}"


def multiplication(a, b):
    return f"Result: {a * b}"


def grading(a, b):
    return f"Result: {a ** b}"


def main():
    operations = ["1.Addition", "2.Subtraction", "3.Multiplication", "4.Division", "5.Grading", "6.Quit"]
    menu = "\n".join(operations)
    print(menu)

    while True:
        command = int(input("Choose the desired operation:"))
        if command == 6:
            print("Goodbye!")
            break
        if command == 1:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number"))
            print(addition(first_number, second_number))
        elif command == 2:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number"))
            print(subtraction(first_number, second_number))
        elif command == 3:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number"))
            print(multiplication(first_number, second_number))
        elif command == 4:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number"))
            print(division(first_number, second_number))
        elif command == 5:
            first_number = float(input("Enter first number:"))
            second_number = float(input("Enter second number"))
            print(grading(first_number, second_number))


main()
