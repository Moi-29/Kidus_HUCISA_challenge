def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


num = int(input("enter the number"))
result = calculate_factorial(num)
print(result)
