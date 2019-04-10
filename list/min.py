def min_to_beginning(numbers: list) -> list:
    numbers.insert(0, min(numbers))
    return numbers


a = [342, 5465, 32, 54, 54765, 545]

print(min_to_beginning(numbers=a))