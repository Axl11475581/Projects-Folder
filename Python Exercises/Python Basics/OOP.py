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
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')


player1 = PlayerCharacter('Cindy')

print(player1)
