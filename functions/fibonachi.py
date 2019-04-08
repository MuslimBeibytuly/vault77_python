def fib_loop(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    temp1: int = 1
    temp2: int = 1
    cnt: int = 2
    while cnt < n:
        temp: int = temp2
        temp2 = temp1 + temp2
        temp1 = temp
        cnt += 1
    return temp2

def fib_rec(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_loop(10))
print(fib_rec(10))

