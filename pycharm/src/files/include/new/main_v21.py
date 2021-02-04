try:
    with open('123.txt', mode='r') as my_file:
        my_file.seek(0)
        print(my_file.read())
except FileNotFoundError as fnf_err:
    print('File Not Found Error')
    raise fnf_err
except IOError as io_err:
    print('Input / Output Error')
    raise io_err
