# match_case_calculator.py

# Get user input for the two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

# Get user input for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is [result].")
    case "-":
        result = num1 - num2
        print(f"The result is [result].")
    case "*":
        result = num1 * num2
        print(f"The result is [result].")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is [result].")
    case _:
        print("Invalid operation. Please choose from (+, -, *, /).")