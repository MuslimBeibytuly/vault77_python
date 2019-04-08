print('enter a: ')
a = int(input())
print('enter b: ')
b = int(input())
print('enter operation: ')
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/':
    print(a / b)
elif op == '*':
    print(a * b)
else:
    print('invalid operation')
