# Adam Jacobs 
# Milestone 4 - Online Shopping Cart 
# This file is a Milestone 4 Project for the Final Online Shopping Cart Project
# Requirements:
#    Step 1: Build the ItemsToPurchase class
#    Step 2: Main Program Implementation
#    Step 3: Output the Total Cost


#Step 1: Build the ItemsToPurchase class
# Created the ItemToPurchase class with the following attributes: item name, price, and quantity.
# Created print_item_cost that prints the item name, quantity, price, and total cost of the item 
class ItemToPurchase:
    def __init__(self):
            self.item_name = "none"
            self.item_price = 0.0
            self.item_quantity = 0
            self.item_description = "none"
    def print_item_cost(self):
            item_cost = self.item_price * self.item_quantity
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:,.2f} = ${item_cost:,.2f}")
    def print_item_description(self):
            print(f" Description:{self.item_description}")

#Step 2: Main Program Implementation
# Created a main function that prompts the user to enter 2 item name, price, and quantity
# Created 2 objects created from unser input and stored in the ItemToPurchase class
def main():
   
        print("Item 1")
        item_1 = input("Enter the item name: ")
        price_1 = float(input("Enter the item price: "))
        quantity_1 = int(input("Enter the item quantity: "))

        item1 = ItemToPurchase()
        item1.item_name = item_1
        item1.item_price = price_1
        item1.item_quantity = quantity_1
        print()

        print("Item 2")
        item_2 = input("Enter the item name: ")
        price_2 = float(input("Enter the item price: "))
        quantity_2 = int(input("Enter the item quantity: ")) 

        item2 = ItemToPurchase()
        item2.item_name = item_2
        item2.item_price = price_2
        item2.item_quantity = quantity_2

#Step 3: Output the Total Cost
#Creating output of the total cost of the items 

        print()
        print("RECEIPT")
        print("TOTAL COST")
        item1.print_item_cost()
        item2.print_item_cost()
        total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
        print(f"Total: ${total_cost:,.2f}")
main()