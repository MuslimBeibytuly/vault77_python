class Field:
    def __init__(self):
        self.value: str = '_'
class Matrix:
    def __init__(self):
        self.fields: list = []
        for i in range(3):
            self.fields.append([])
            for j in range(3):
                self.fields[i].append(Field())
    
class Game:
    def __init__(self):
        self.matrix = Matrix()
    def show(self):
        cnt = 0
        for column in self.matrix.fields:
            headers = '|'.join(
                [str(cnt + 1), str(cnt + 2), str(cnt + 3)]
            )
            print(headers)
            row = '|'.join([field.value for field in column])
            print(row)
            cnt += 3

    def is_field_empty_by(self, number: int) -> bool:
        valid = self.matrix.fields[
            (number - 1) // 3
        ][
            (number - 1) % 3
        ].value == '_'
        if not valid:
            print('Area is not empty, please choose another')
        return valid
    
    def is_valid(self, number: int) -> bool:
        if number >= 1 and number <= 9 and \
            self.is_field_empty_by(number=number):
            return True
        return False

    def assign(self, number: int, sign: str) -> None:
        self.matrix.fields[
                (number - 1) // 3
            ][
                (number - 1) % 3
            ].value = sign

    def someone_wins(self):
        for column in self.matrix.fields:
            row = ''.join([field.value for field in column])
            if 'X' * 3 == row:
                return True, 'X'
            if '0' * 3 == row:
                return True, '0'
        for index in range(3):
            sum_of_column = ''
            for column in range(
                len(self.matrix.fields)
            ):
                sum_of_column += self.matrix.fields[
                    column
                ][
                    index
                ].value
            if 'X' * 3 == sum_of_column:
                return True, 'X'
            if '0' * 3 == sum_of_column:
                return True, '0'
        left = ''
        right = ''
        for i in range(3):
            left += self.matrix.fields[i][i].value
            right += self.matrix.fields[i][2 - i].value
        if 'X' * 3 == left or 'X' * 3 == right:
            return True, 'X'
        if '0' * 3 == left or '0' * 3 == right:
            return True, '0'
        return False, ''
    
    def run(self):
        step = 0
        while True:
            step += 1
            self.show()
            number = int(input())
            while not self.is_valid(number=number):
                number = int(input())
            sign = 'X' if step % 2 == 1 else '0'
            self.assign(number, sign)
            winned, winner = self.someone_wins()
            if winned:
                print(f'You won {winner}')
                return

class Player:
    pass

if __name__ == "__main__":
    game = Game()
    game.run()
