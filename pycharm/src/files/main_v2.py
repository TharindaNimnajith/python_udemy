# no need to close when open the file this way

# default mode is 'r' for read
# with open('test.txt') as my_file:

with open('test.txt', mode='r') as my_file:
    print(my_file)

    print('---------------------')

    print(my_file.read())

    # can only read the file once
    # because cursor is at the end of the file
    print(my_file.read())
    print(my_file.read())

    print('---------------------')

    # set the cursor to the beginning of the file
    my_file.seek(0)
    print(my_file.read())
    my_file.seek(0)
    print(my_file.read())

    print('---------------------')

    my_file.seek(0)
    print(my_file.readline())

    print('---------------------')

    my_file.seek(0)
    print(my_file.readline())
    print(my_file.readline())

    print('---------------------')

    my_file.seek(0)
    print(my_file.readlines())
