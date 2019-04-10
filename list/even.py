def get_even(l: list) -> list:
    evens = []
    for element in l:
        if element > 0:
            evens.append(element)
    return evens

print(
    get_even(
        l=[1, -2, 3, 4, -5]
    )
)
print(
    get_even(
        l=(-1, 2, 3, -4, 5)
    )
)
