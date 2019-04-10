# 5
# 2
# 0, 1, 2, 3, 4, 5
def median(elements: list) -> float:
    if len(elements) % 2 == 1:
        m = elements[
            int(
                (len(elements) - 1) / 2
            )
        ]
    else:
        first = elements[
            int(len(elements) / 2 - 1)
        ]
        second = elements[
            int(len(elements) / 2)
        ]
        m = (first + second) / 2.0
    return m

print(median([1, 2, 3, 4]))