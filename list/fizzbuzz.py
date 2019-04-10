def fizzbuzz(n: int) -> list:
    return [
        (
            'fizz' * int(
                cnt % 2 == 0
            ) + 'buzz' * int(
                cnt % 3 == 0
            )
        ) or str(cnt)
        for cnt in range(n)
    ]

print(fizzbuzz(20))
