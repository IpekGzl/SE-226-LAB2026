from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

while True:
    data = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

    try:
        parts = data.split(",")
        parts = strip_whitespaces(parts)

        numbers = [float(x) for x in parts]

        numbers = remove_duplicates(numbers)

        print(f"Cleaned and unique data: {numbers}")
        print("--------------------")
        print(f"Mean: {calculate_mean(numbers):.2f}")
        print(f"Maximum: {find_maximum(numbers)}")
        print(f"Minimum: {find_minimum(numbers)}")

    except:
        print("Data Error: Please make sure you only enter numbers separated by commas.")
