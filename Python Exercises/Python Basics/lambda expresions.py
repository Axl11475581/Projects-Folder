# lambda expressions are one time anonymous functions that only need to run once

# Square
my_list = [5, 4, 3]
new_list = list(map(lambda num: num**2, my_list))
print(new_list)

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
