def min_of_2(a: int, b: int) -> int:
    if a > b:
        return b
    return a

def min_of_4(a: int, b: int, c: int, d: int) -> int:
    temp = a
    if temp > a:
        temp = a
    if temp > b:
        temp = b
    if temp > c:
        temp = c
    if temp > d:
        temp = d
    return temp
    # return min_of_2(
    #     a=min_of_2(a=a, b=b), # 2 
    #     b=min_of_2(a=c, b=d)  # 3
    # )

print(min_of_4(1, 2, 3, 4))
