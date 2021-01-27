# walrus operator (:=)

# new syntax introduced in python 3.8
# assigns values to variables as a part of a larger expression


a = 'Hello World!'

if len(a) > 10:
    print(f'Element \'{a}\' is too long ({len(a)} characters).')
else:
    print(f'Element \'{a}\' is OK.')


a = 'Hello World!'

# noinspection PyRedundantParentheses
if ((n := len(a)) > 10):
    print(f'Element \'{a}\' is too long ({n} characters).')
else:
    print(f'Element \'{a}\' is OK.')


a = 'Hello World!'

if (n := len(a)) > 10:
    print(f'Element \'{a}\' is too long ({n} characters).')
else:
    print(f'Element \'{a}\' is OK.')


a = 'Hello World!'

if n := len(a) > 10:
    print(f'Element \'{a}\' is too long ({n} characters).')
else:
    print(f'Element \'{a}\' is OK.')


a = 'Hello World!'

if n := len(a) > 10:
    print(n)


a = 'Hello World!'

# noinspection PyRedundantParentheses
if (n := len(a) > 10):
    print(n)


a = 'Hello World!'

if n := (len(a) > 10):
    print(n)


a = 'Hello World!'

if (n := len(a)) > 10:
    print(n)


a = 'Hello World!'

while (n := len(a)) > 1:
    print(n)
    print(a[n - 1])
    a = a[:-1]

print(n)
print(a)
