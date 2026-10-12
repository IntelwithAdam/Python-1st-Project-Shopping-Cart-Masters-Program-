# Adam Jacobs 
# Milestone 2 - Project Initialization and Variable Setup 
# This file is a Milestone 2 Project for the Final Online Shopping Cart Project
# Requirments: 
#    Initialize script meaning create the .py file
#    Implement input() statements to gather data from the user being a shopper
#    Assign gathered data inputs with apropriate named variables
#    Perform at least two basic arithmetic expressions using the gathered data

#Import the products.py file to access the product names and prices
import products 

# Display Product Options and Prices to Shopper
print("\n""Available Product Selection Below:", "\n")
print(f"\tHeadphones: $ {products.headphones:.2f}")
print(f"\tLaptop: $ {products.laptop:,.2f}")
print(f"\tMouse: $ {products.mouse:.2f}")
print(f"\tT-Shirt: $ {products.tshirt:.2f}")
print(f"\tPants: $ {products.pants:.2f}")
print(f"\tSocks: $ {products.socks:.2f}")
print(f"\tShoes: $ {products.shoes:.2f}")

# Gathered shoppers data via input() statements and assign to appropriate named variables
#Gather Product 1
print ("\n""Please enter the product information below:""\n")
product1_name = input("\t""Enter Product Name:")
product1_price = float(input("\t""Enter Product Price:"))
product1_quantity = int(input("\t""Enter Quantity:"))

#Gather Product 2
print ("\n""Please enter the 2nd product information below:""\n")
product2_name = input("\t""Enter Product Name:")
product2_price = float(input("\t""Enter Product Price:"))
product2_quantity = int(input("\t""Enter Quantity:"))

#Product 1 Subtotal Calculation using multiplication
product1_subtotal = product1_price * product1_quantity
print("\n""Shopping Cart Summary:")
print(f"\tProduct 1 Subtotal: $ {product1_subtotal:,.2f}")

#Product 2 Subtotal Calculation using multiplication
product2_subtotal = product2_price * product2_quantity
print(f"\tProduct 2 Subtotal: $ {product2_subtotal:,.2f}")

#Cart Total Calculation using addition
total = product1_subtotal + product2_subtotal
print(f"\tCart Total: $ {total:,.2f}")