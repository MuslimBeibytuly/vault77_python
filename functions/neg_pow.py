def neg_pow(a: float, n: int) -> float:
    cnt: int = 0
    res: float = 1.0
    while cnt > n:
        res /= a
        cnt -= 1
    return res

print(neg_pow(a=2.0, n=-3))
