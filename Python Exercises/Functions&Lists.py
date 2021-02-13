# list of strings
food = ["hamburger", "pizza", "sushi", "ribs", "fries"]

# list of ints
prices = [5.65, 9.99, 4.88, 7.00, 11.99]

# insert elements to an existing list
food.insert(2, "spaghetti")

# extend an existing list (name of the 2nd list to add)
food.extend(prices)

# find elements in a list
print(food.index("pizza"))

# count the numbers of times an element is repeated in a list
print(food.count("pizza"))

# copy a list (random is the name of the new list)
random = food.copy() + prices.copy()

# display the list
print(food)
