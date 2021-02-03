from random import randint
from sys import argv

answer = 0

while True:
    try:
        answer = randint(int(argv[1]), int(argv[2]))
        break
    except ValueError:
        print('Please enter two integers and try again.')
        exit()

while True:
    try:
        guess = int(input(f'Guess a number in {argv[1]}~{argv[2]} range: '))
        if 1 <= guess <= 10:
            if guess == answer:
                print('Correct!')
                break
            else:
                print('Try again!')
        else:
            print('Need a number in 1~10 range.')
    except ValueError:
        print('Please enter a number.')
        continue

# run on terminal using a command similar to the below command.
# py guessing_game.py 1 10
