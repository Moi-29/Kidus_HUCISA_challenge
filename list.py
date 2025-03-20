def list_operations(numbers):
    print(f"Original list: {numbers}")
    # to add a number to the list
    new_number = int(input("Enter a number to add: "))
    numbers.append(new_number)
    print(f"List after adding {new_number}: {numbers}")
    # to remove the number from list
    remove_number = int(input("Enter a number to remove: "))
    if remove_number in numbers:
        numbers.remove(remove_number)
        print(f"List after removing {remove_number}: {numbers}")
    else:
        print(f"{remove_number} is not in the list.")
        # to calculate the numbers max and min value
    if len(numbers) > 0:
        max_value = max(numbers)
        min_value = min(numbers)
        print(f"Maximum value: {max_value}")
        print(f"Minimum value: {min_value}")
    else:
        print("The list is empty.")


numbers = [2, 4, 6, 8, 10]
list_operations(numbers)
