import sys
from random import randint

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'Guess a number {sys.argv[1]}~{sys.argv[2]}: '))
        if 0 < guess < 11:
            if guess == answer:
                print('Correct!')
                break
        else:
            print('Need a number in 1~10 range.')
    except ValueError:
        print('Please enter a number.')
        continue
