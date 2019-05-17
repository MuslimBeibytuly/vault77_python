class Question:
    def __init__(self, text: str, variants: list, right: int):
        self.text = text
        self.variants = variants
        self.right = right

    def is_right(self, variant: int):
        return variant == self.right

class Quiz:
    def __init__(self):
        with open('questions.txt', 'r') as file:
            self.questions = []
            lines = file.readlines()
            for line in lines:
                elements = line.split('|')
                variants = [
                    elements[1], elements[2], elements[3], elements[4]
                ]
                question = Question(
                    elements[0],
                    variants,
                    elements[5]
                )
                self.questions.append(question)
        self.score = 0

class Game:
    def __init__(self):
        self.quiz = Quiz()
    
    def show(self):
        for question in self.quiz.questions:
            print(question.text)
            print(question.variants)


if __name__ == "__main__":
    game = Game()
    game.show()
