def dictionary_manipulation():
    students = {"Alice": 20, "Bob": 21, "Charlie": 19}

    print("Original dictionary:")
    for name, age in students.items():
        print(f"{name}: {age}")

    new_name = input("Enter the name of the new student: ")
    new_age = int(input("Enter the age of the new student: "))
    students[new_name] = new_age
    print(f"\nDictionary after adding {new_name}:")
    for name, age in students.items():
        print(f"{name}: {age}")

    update_name = input("\nEnter the name of the student to update: ")
    if update_name in students:
        new_age = int(input("Enter the new age: "))
        students[update_name] = new_age
        print(f"\nDictionary after updating {update_name}'s age:")
        for name, age in students.items():
            print(f"{name}: {age}")
    else:
        print(f"{update_name} is not in the dictionary.")

    remove_name = input("\nEnter the name of the student to remove: ")
    if remove_name in students:
        del students[remove_name]
        print(f"\nDictionary after removing {remove_name}:")
        for name, age in students.items():
            print(f"{name}: {age}")
    else:
        print(f"{remove_name} is not in the dictionary.")


dictionary_manipulation()
