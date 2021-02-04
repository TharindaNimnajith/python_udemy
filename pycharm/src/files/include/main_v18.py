with open('D:\\python_udemy\\pycharm\\src\\files', mode='a+') as my_file:
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.read())
