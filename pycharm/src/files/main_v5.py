with open('sad.txt', mode='w') as my_file:
    text = ':-('
    return_value = my_file.write(text)
    print(return_value)
    print(len(text))

# 'w' creates the file if not exists
