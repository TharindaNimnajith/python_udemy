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


# 3. Print out: 'The oldest cat is x years old.' - x will be the
# oldest cat age by using the function in #2.
print(f'The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.')


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
print(super_list1[0])

print(issubclass(list, object))


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
