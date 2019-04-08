# 2, 3
def pow(a: float, n: int) -> float:
    cnt: int = 0
    res: float = 1.0
    while cnt < n:
        res = res * a # 2, 4, 8
        cnt = cnt + 1 # 1, 2, 3
    return res

def pow_rec(a: float, n: int) -> float:
    if n == 1:
        return a
    return a * pow_rec(a, n - 1)

print(pow_rec(2, 3))

def xor(x: bool, y: bool) -> bool:
    result = False
    if not x and not y:
        result = False
    elif x and y:
        result = False
    else:
        result = True
    return result
