number = 10

guessed = int(input())

while guessed != number:
    if guessed < number:
        print('Guess higher')
    else:
        print('Guess lower')
    guessed = int(input())
print('You\'re right')
