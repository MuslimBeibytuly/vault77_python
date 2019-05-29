class Field:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

class Snake:
    def __init__(self):
        self.fields = (
            Field(5, 5, '*'),
            Field(5, 6, '*'),
            Field(5, 7, '*'),
            Field(5, 8, '*')
        )
    def draw(self):
        for i in range(10):
            for j in range(10):
                for field in self.fields:
                    if i == field.x and j == field.y:
                        print(field.sign, end='')
                    else:
                        print(' ', end='')
            print()

if __name__ == '__main__':
    Snake().draw()
