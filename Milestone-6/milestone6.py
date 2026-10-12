# Adam Jacobs 
# Milestone 6 - Online Shopping Cart - Part 2
# This file is a Milestone 6 Project for the Final Online Shopping Cart Project
# Requirements:
#    Step 4: Build the ShoppingCart class
#    Step 5: User Interface - Menu Options
#    Step 6: User Interface - Loop

#Step 1: Milestone 4 - ItemsToPurchase class
#added Description attribute to the ItemToPurchase class
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
            print(f"    Description: {self.item_description}")

#Step 4: Build the ShoppingCart class
#Created the ShoppingCart class with the following attributes: customer name, current date, and cart items.

class ShoppingCart:    
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

 # Defined add_item (ItemToPurchase) method that adds an item to the shopping cart.
 #  self: refers to the ShoppingCart 
 #  item: an item of the ItemToPurchase class to be added 
 #  .append: adds the item to the end of the self.cart_items list
    def add_item(self, item_to_add):
        self.cart_items.append(item_to_add)

# Defined the remove_item method to remove an existing item from the shopping cart.
# For loop and if statement: We are searching for item_name equal to searched item in the self.cart_items list.
# break exits the loop after the item is removed and skips the else statement.
# else if not found, it prints a message that the item was not found in the cart.
    def remove_item(self, item_name):
        for item_to_remove in self.cart_items:
            if item_to_remove.item_name == item_name:
                self.cart_items.remove(item_to_remove)
                break
        else:   
            print("Item not found in cart. Nothing removed.")

#Defined the modify_item (ItemToPurchase) method that modifies an existing item in the shopping cart.
#for loop searches through existing shopping cart item for the matching item name, that need to be modified. 
#if the existing cart item matches the itemname, modify it by updating the price and quantity.
#break exits the loop after the item is modified and skips the else statement.
#else print if the item is not found in the cart, it prints a message indicating that nothing was modified.
    def modify_item(self, item_to_modify):
        for existing_item in self.cart_items:
            if existing_item.item_name == item_to_modify.item_name:
                if item_to_modify.item_price > 0:
                    existing_item.item_price = item_to_modify.item_price
                existing_item.item_quantity = item_to_modify.item_quantity
                break
        else:   
            print("Item not found in cart. Nothing modified.")

#Defined the get_num_items_in_cart method that returns the total quantity of items in the shopping cart.
#Starts with  total_quantity_in_cart = 0 and adds each item quantity to it.
#for loop goes through the cart_items list and adds each item quantity to the total_quantity_in_cart variable.
#returns the total quantity of items in the shopping cart.
    def get_num_items_in_cart(self):
        total_quantity_in_cart = 0
        for quantity_item in self.cart_items:
            total_quantity_in_cart = total_quantity_in_cart + quantity_item.item_quantity
        return total_quantity_in_cart

#Defined the get_cost_of_cart method that returns the total cost of all items in the shopping cart.
#Starts with total_cost_of_cart = 0 and adds each item cost to it.
#for loop goes through the cart_items list and adds each item cost to the total_cost_of the cart variable.
    def get_cost_of_cart(self):
        total_cost_of_cart = 0
        for cost_item in self.cart_items:
            total_cost_of_cart = total_cost_of_cart + (cost_item.item_price * cost_item.item_quantity)
        return total_cost_of_cart

#Defined a print_total method displays the full cart or SHOPPING CART IS EMPTY 
#Full cart displays the customer name, cart items, current date, total quantity in cart, and the total cost of all items in the cart.
#print_descriptions method displays each item desciption in the cart. 
    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print(f"{self.customer_name} Shopping Cart on {self.current_date}")
            print("SHOPPING CART IS EMPTY")
            print(f"Total: ${self.get_cost_of_cart():,.2f}")
        else:
            print(f"{self.customer_name} Shopping Cart on {self.current_date}")
            print(f"Total Number of Items: {self.get_num_items_in_cart()}")
            print()
            print("ITEMS IN CART:")
            for display_item in self.cart_items:
                display_item.print_item_cost()
                display_item.print_item_description()
            print()
            print(f"Total: ${self.get_cost_of_cart():,.2f}")

#Defined a print_descriptions method that displays each item description in the cart.
    def print_descriptions(self):
        print(f"{self.customer_name} Shopping Cart on {self.current_date}")
        print()
        print("ITEMS' DESCRIPTIONS")
        for display_item in self.cart_items:
            display_item.print_item_description()

#Step 5: User Interface - Menu Options
#print_menu that allows the user to interact with their cart viea the console.
def print_menu():
    print()
    print("MENU")
    print("a - Add item")
    print("r - Remove item")
    print("c - Change quantity")
    print("i - Items Descriptions")
    print("o - Shopping cart")
    print("q - Quit")

#Step 6: User Interface - While Loop
#While loop that allows the user to interact with their cart via the console until they choose to (q) quit the program.
shopping_cart = ShoppingCart()
interactive_menu = ""
shopping_cart.customer_name = input("Enter Your name: ")
shopping_cart.current_date = input("Enter todays date: ")
print()
while interactive_menu != "q":
    print_menu()
    print()
    interactive_menu = input("Type a letter to choose an option: ")
    print()
    if interactive_menu == "a":
        print("ADD ITEM TO CART")
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
        item_description = input("Enter the item description: ")
        added_item = ItemToPurchase()
        added_item.item_name = item_name
        added_item.item_description = item_description
        added_item.item_price = item_price
        added_item.item_quantity = item_quantity
        shopping_cart.add_item(added_item)
    elif interactive_menu == "r":
        print("REMOVE ITEM FROM CART")
        remove_item_name = input("Enter name of item to remove: ")
        shopping_cart.remove_item(remove_item_name)
    elif interactive_menu == "c":
        print("CHANGE ITEM QUANTITY")
        item_name = input("Enter the item name: ")
        new_quantity = int(input("Enter the new quantity: "))
        modified_item = ItemToPurchase()
        modified_item.item_name = item_name
        modified_item.item_quantity = new_quantity
        shopping_cart.modify_item(modified_item)
    elif interactive_menu == "i":
        print("ITEM'S DESCRIPTIONS")
        shopping_cart.print_descriptions()
    elif interactive_menu == "o":
        print("SHOPPING CART")
        shopping_cart.print_total()




