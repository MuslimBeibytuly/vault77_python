import json

class Question:
    def __init__(self, text: str, variants: list, right: int):
        self.text = text
        self.variants = variants
        self.right = right

class Quiz:
    def __init__(self):
        self.questions = []
        with open('questions.json', 'r') as file:
            questions = json.load(fp=file)['questions']
            for question in questions:
                self.questions.append(
                    Question(**question)
                )

class Game:
    def __init__(self):
        self.__quiz = Quiz()
        self.__score = 0
    
    def greeting(self):
        print('Please answer questions below')
    
    def show_and_answer(self):
        for question in self.quiz.questions:
            print(f'Question is: {question.text}')
            cnt = 0
            for variant in question.variants:
                print(f'{cnt}) {variant}')
                cnt += 1
            answer = int(input())
            if answer == question.right:
                self.score += 1
                print('You\'re right, congrats')
            else:
                print('You\'re wrong, sorry')
        print(f'Your score is: {self.score}')


if __name__ == "__main__":
    game = Game()
    game.show_and_answer()
