import random

hiddenNumber = random.randint(1, 20)
try:
    while True:
        print('I am thinking of a number between 1 and 20.')
        guess = int(input('Enter your guess: '))
        if guess > 20:
            print('Learn to read buddy lol')
        elif guess > hiddenNumber:
            print('Your guess is too high')
        elif guess < hiddenNumber:
            print('Your guess is too low')
        else:
            print('Accurate prediction')
        if guess == hiddenNumber:
            break
except ValueError:
    print('Error. Please enter an integer')