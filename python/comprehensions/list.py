numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [number for number in numbers if number % 2 == 0]
doubled = (number * 2 for number in numbers)

print(evens)
for element in doubled:
    print(element)
