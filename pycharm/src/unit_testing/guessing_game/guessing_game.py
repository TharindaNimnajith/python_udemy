from random import randint


def run_guess(guess_, answer_):
    try:
        if 1 <= guess_ <= 10:
            if guess_ == answer_:
                print('Correct!')
                return True
            else:
                print('Try again!')
                return False
        else:
            print('Need a number in 1~10 range.')
            return False
    except TypeError as error:
        return error


answer = randint(1, 10)

if __name__ == '__main__':
    while True:
        try:
            guess = int(input('Guess a number in 1~10 range: '))
        except ValueError:
            print('Please enter a number.')
            continue
        if run_guess(guess, answer):
            break
