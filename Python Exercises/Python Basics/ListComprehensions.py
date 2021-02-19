# list, set, dictionary (you can use Comprehensions with these)
# Comprehensions are a quick way to create lists or sets or dictionary in Python instead of perhaps looping

# Instead of:
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# One can use List Comprehension to get the same result:
my_list2 = [char for char in 'hello']
my_list3 = [num for num in range(0, 100)]
my_list4 = [num*2 for num in range(0, 100)]

print(my_list2)
print(my_list3)
print(my_list4)

# One can have different functions and checkers inside the [] to do complex iterations in one line
my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list5)
"""
The way it works is: we have an expression (num) of what we want to do with each
item that we're iterating over, then we loop through using a for loop through an 
iterable, we give it a variable that we're gonna act upon, and then if we want we 
also have an option to add a conditional at the end to check before adding it to the list.
"""
