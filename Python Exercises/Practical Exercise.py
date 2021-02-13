# 7 Exercise to practice the previous topics viewed 1

price_product_1 = input("What is the price of the product 1?: \n ")
quantity_product_1 = input("How many of the product 1 will you buy?: \n ")
price_product_2 = input("What is the price of the product 2?: \n ")
quantity_product_2 = input("How many of the product 2 will you buy?: \n ")
price_product_3 = input("What is the price of the product 3?: \n ")
quantity_product_3 = input("How many of the product 3 will you buy?: \n ")

result_product_1 = float(price_product_1)*float(quantity_product_1)
result_product_2 = float(price_product_2)*float(quantity_product_2)
result_product_3 = float(price_product_2)*float(quantity_product_3)

result = result_product_1+result_product_2+result_product_3
print("Your final price is: \n" + str(result))

# Exercise to practice the previous topics viewed 2

name_1 = input("Write your name: \n")
name_2 = input("Write your name: \n")
name_3 = input("Write your name: \n")

slices_in_pizza = input("How many slices had the pizza?: \n")
pizza_price = input("How much did the pizza cost? \n")

percentage_ate_by_person_1 = input(name_1 + "How many slices did you ate?: \n")
percentage_ate_by_person_2 = input(name_2 + "How many slices did you ate?: \n")
percentage_ate_by_person_3 = input(name_3 + "How many slices did you ate?: \n")

number_of_slices_ate_by_person_1 = float(percentage_ate_by_person_1)*float(slices_in_pizza)
number_of_slices_ate_by_person_2 = float(percentage_ate_by_person_2)*float(slices_in_pizza)
number_of_slices_ate_by_person_3 = float(percentage_ate_by_person_3)*float(slices_in_pizza)

price_paid_by_name_1 = float(percentage_ate_by_person_1)*float(pizza_price)
price_paid_by_name_2 = float(percentage_ate_by_person_2)*float(pizza_price)
price_paid_by_name_3 = float(percentage_ate_by_person_3)*float(pizza_price)

print(name_1 + " have ate " + str(number_of_slices_ate_by_person_1) + " of slices, and paid " + str(price_paid_by_name_1) + "$ for the meal")
print(name_2 + " have ate " + str(number_of_slices_ate_by_person_2) + " of slices, and paid " + str(price_paid_by_name_2) + "$ for the meal")
print(name_3 + " have ate " + str(number_of_slices_ate_by_person_3) + " of slices, and paid " + str(price_paid_by_name_3) + "$ for the meal")