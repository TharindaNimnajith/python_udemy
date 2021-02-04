try:
    with open('include.txt', mode='x') as my_file:
        my_file.seek(0)
        print(my_file.read())
except FileNotFoundError as fnf_err:
    print('File Not Found Error')
    raise fnf_err
except IOError as io_err:
    print('Input / Output Error')
    raise io_err

# 'x' opens a file for exclusive creation.
# if the file already exists, the operation fails.
