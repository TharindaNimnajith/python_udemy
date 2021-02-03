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


import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
