with open('test.txt', mode='r') as my_file:
    text = 'I am fine!'
    return_value = my_file.write(text)
    print(return_value)
    print(len(text))
