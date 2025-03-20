class MathOperations:
    def add(self, num1, num2, num3=0):
        return num1 + num2 + num3


if __name__ == "__main__":
    math_ops = MathOperations()
    sum_two = math_ops.add(5, 7)
    print(f"Sum of two numbers: {sum_two}")
    sum_three = math_ops.add(5, 7, 3)
    print(f"Sum of three numbers: {sum_three}")
