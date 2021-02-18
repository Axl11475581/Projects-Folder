# OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

"""
What is an object? Objects have methods like these and attributes
that you can access with the DOT method. Now OOP allows the programmer to 
go beyond what Python just gives us (these data types) and create out own.
Why is this useful? OOP is a paradigm, it's a way for us to think about our
code and structure in a way that is easier to maintain, extend and write.
"""

# Example of a created class
""""
self refers to the player character that is created in line 30. 
The class PlayerCharacter is the blueprint of what we want to create,
the basic attributes and the properties that the class has, the methods
or actions that the class can do. Then with the blueprint ready you can 
create different objects (in this case the player1 in line 30) in programming
terms: We just instantiate the class PlayerCharacter in the player1 instance.
"""


class PlayerCharacter:
    membership = True  # This is a Class Object Attribute, a static (unchangeable) characteristic.

    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')


# All the objects that are instantiated will have the Object Attribute


player1 = PlayerCharacter('Cindy')

print(player1)


# OOP Exercise 'Cat'
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Bianca = Cat('Bianca', 6)
Max = Cat('Max', 4)
Lulu = Cat('Lulu', 2)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(Bianca.age, Max.age, Lulu.age)} years old.")


# OOP Exercise 2

class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
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


# 1 Add another Cat

class Bianca(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Bianca('Bianca', 6)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()