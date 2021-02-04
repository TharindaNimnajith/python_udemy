with open('test.txt', mode='a+') as my_file:
    text = '\nI am fine!'
    my_file.write(text)
    my_file.write(text)
