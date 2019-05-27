# 90-95%
# Object oriented programming
class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f'I\'m {self.name} and I\'m eating')

    def sleep(self):
        print(f'I\'m {self.name} and I\'m sleeping')

class Worker(Human):
    def __init__(
        self, name: str, age: int, gender: str, job: str
    ):
        super().__init__(name, age, gender)
        self.job = job

    def sleep(self):
        print(f'I\'m {self.name} and I sleep 10 hours a day')
    
    def work(self):
        print(f'I\'m {self.name} and I\'m working')

class Student(Human):
    def sleep(self):
        print(
            f'I\'m {self.name} and I sleep 5 hours a day'
        )

class Button:
    def __render(self):
        pass

if __name__ == '__main__':
    human1 = Human('Muslim', 22, 'M')
    human1.eat()
    human1.sleep()
    human2 = Worker('LOL', 1, 'F', 'builder')
    human2.eat()
    human2.sleep()
    human3 = Student('LOL', 1, 'F')
    human3.eat()
    human3.sleep()
# encapsulation - сокрыти_fillе данных и методов
# abstraction - высокоуро_fillвневые абстракции
# polymorphism - множественная реализация и общий интерфейс
# inheritance - наследование: DRY - don't repeat yourself


class Car:
    def __init__(self):
        self._radiator = 'I\'m radiator'
    
    def _fill(self):
        self._radiator = 'I\'m full radiator'
    
    def greet(self):
        self._fill()

# __ - don't touch
# _ - sometimes allowed to touch
