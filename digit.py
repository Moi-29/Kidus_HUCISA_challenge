def count_digits(number):
    return len(str(abs(number)))


number = int(input("Enter your digit: "))
print(f"The number {number} has {count_digits(number)} digits.")
