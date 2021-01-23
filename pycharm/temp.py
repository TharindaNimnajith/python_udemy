def highest_even(list_):
    evens = []
    for list_item in list_:
        if list_item % 2 == 0:
            evens.append(list_item)
    return max(evens)

print(highest_even([10, 1, 2, 3, 4, 8]))


# Scope - what variables do I have access to?

def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)

outer()

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions


print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))


class BigObject:
    pass

obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))


# Add 3 more magic / dunder methods of your choice to this Toy class.
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoo',
            'has_pets': False,
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        return 'deleted'

    def __call__(self):
        return 'yes?'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])


class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
print(super_list1[0])

print(issubclass(list, object))


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1. Instantiate the Cat object with 3 cats.
peanut = Cat('Peanut', 3)
garfield = Cat('Garfield', 5)
snickers = Cat('Snickers', 1)

# 2. Create a function that finds the oldest cat.
def get_oldest_cat(*args):
    return max(args)

# 3. Print out: 'The oldest cat is x years old.' - x will be the oldest cat age by using the function in #2.
print(f'The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.')


class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create a list of all of the pets (create 3 cat instances from the above).
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

# Instantiate the Pet class with all your cats.
my_pets = Pets(my_cats)

# Output all of the cats singing using the my_pets instance.
my_pets.walk()


from functools import reduce

# Capitalize all of the pet names and print the list.
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

# Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# Filter the scores that pass over 50%.
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))

# Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores).
# What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))


print(list(map(lambda num: num**2, [1, 2, 3])))

a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print(a)


# performance decorator

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}')
        return result

    return wrapper

@performance
def long_time():
    for i in range(10000):
        i * 5

long_time()


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

user1 = {'name': 'Sorna', 'valid': True}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)


from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result

    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5

long_time()
long_time2()


def special_for(iterable):
  iterator = iter(iterable)

  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break

class MyGen:
  current = 0

  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first  # this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1, 100)

for i in gen:
    print(i)


# generator which calculates fibonacci numbers:

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(100):
    print(x)

def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(100))


import sys

print(sys.path)


from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue


def do_stuff(num=0):
  try:
    if num:  # try to test for when input is 0. How can you fix this?
      return int(num) + 5
    else:
      return 'please enter number'
  except ValueError as err:
    return err


import random

def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = '<to email address>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')


import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))


import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = 'zerotomastery'
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

# Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'User name here':
    print(follower.name)
    follower.follow()


# Be a narcissist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


#([A-Za-z0-9$%#@]{7,}[0-9])


# MRO - Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass


a = 'helloooooooooo'

if (n := len(a)) > 10:
    print(f'too long {n} elements')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)


import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
