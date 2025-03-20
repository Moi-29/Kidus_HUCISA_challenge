def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str


input_str = input("enter the str: ")
print(f"Original string: {input_str}")
print(f"Reversed string: {reverse_string(input_str)}")
