# def sign(x: int) -> str:
#     if x >= 0:
#         return '+'
#     return '-'

# def concat_int_and_str(
#     a = 2,
#     b = ' is two'
# ):
#     result = str(a) + b
#     return result

# print(concat_int_and_str(a=1, b='is one'))
# print(concat_int_and_str())

# def doubled(a):
#     return a * 2

# x = -1
# y = doubled(x)
# print('doubled x is: ' + str(y))

# def say_hello():
#     print('hello')

# say_hello()

# def return_5():
#     return 5

# print(return_5())

# def say_hello_to(name):
#     print('hello, ' + name)

# say_hello_to('Muslim')

# def empty():
#     # TODO: implement this function
#     pass
# empty()

# def add(a, b):
#     # return 4
#     return a + b

# def make_operation(a, b, operate):
#     # a = 1, b = 3, operate = add
#     # add(1, 3)
#     return operate(a, b)

# result = make_operation(a=1, b=3, operate=add)

# print('result is ' + str(result))

# def factorial(n: int) -> int:
#     result = 1
#     temp = 1
#     while temp <= n:
#         result = result * temp
#         temp = temp + 1
#     return result

# print(factorial(5))

def sum_to_n(n):
    if n > 0:
        return n + sum_to_n(n - 1)
    return n

print(sum_to_n(5))
