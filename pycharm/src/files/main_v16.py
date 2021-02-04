with open('include/include.txt', mode='a+') as my_file:
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.read())
