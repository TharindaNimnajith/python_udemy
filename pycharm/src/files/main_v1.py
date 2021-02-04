my_file = open('test.txt')
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

my_file.close()

print('---------------------')

print(my_file.read())
