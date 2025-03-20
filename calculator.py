def simple_calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")


simple_calculator()
