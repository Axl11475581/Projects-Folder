def per_1(name):
    print(name + ": hello how can I help you?")


def per_2_1(food, drink, dessert, name):
    name = input("What is your name?: \n")
    food = input("What do you want to eat?: \n")
    drink = input("And to drink?: \n")
    dessert = input("And finally, what would you like for dessert? \n")

    print(name + ": and I would like to eat " + food + " and for the drink I will go with " + drink + " and finally " + dessert + " as dessert.")


def per_1_2(name):
    print(name + ": thank you.")


per_1("Cashier")
per_2_1("food", "drink", "dessert", "name")
per_1_2("Cashier")
