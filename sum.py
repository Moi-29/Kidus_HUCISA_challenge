def sum_of_even_numbers():
    total_sum = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total_sum += num

    print(f"The sum of even numbers from 1 to 100 is: {total_sum}")


sum_of_even_numbers()
