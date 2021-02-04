with open('./include.txt', mode='a+') as my_file:
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.read())

with open('./../sad.txt', mode='a+') as my_file:
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.read())

with open('./new/include.txt', mode='a+') as my_file:
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.read())
