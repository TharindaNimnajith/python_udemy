from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number in 1~10 range: '))
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
