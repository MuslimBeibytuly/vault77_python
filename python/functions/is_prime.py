def is_prime(number: int) -> bool:
    temp: int = 2
    while temp < number:
        if number % temp == 0:
            return False
        temp += 1
    return True

print(is_prime(10))
print(is_prime(5))
