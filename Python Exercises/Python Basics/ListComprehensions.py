# list, set, dictionary (you can use Comprehensions with these)
# Comprehensions are a quick way to create lists or sets or dictionary in Python instead of perhaps looping

# Instead of:
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# One can use List Comprehension to get the same result:
my_list2 = [char for char in 'hello']

print(my_list2)
