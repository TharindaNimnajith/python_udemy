try:
    with open('include.txt', mode='r') as file:
        for i in range(21):
            print(file.read(4))
except FileNotFoundError as err:
    print(f'File not found error: {err}')
except IOError as err:
    print(f'IO error: {err}')
