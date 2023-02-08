# Libraries

# Library 1: Pandas
# Pandas is used to present tabular data to the user
import pandas as pd


#========The beginning of the class==========
# The shoe class is used to identify each item in the inventory as a shoe and identify relevent qualitities of the item
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        pass
        return self.cost

    def get_quantity(self):
        pass
        return self.quantity

    def __str__(self):
        pass
        return f"{self.product} from {self.country}, code: {self.code}, cost: {self.cost}, quantity: {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#=============Headers list===========
'''
The list will be used to store a list of objects of headers.
'''
headers = []

#=============Menu Selection===========
'''
The list will be used to store the menu option.
'''
menu_option = ""

#==========Functions outside the class==============
#  Read shoes data attempts to read the data from the inventory file and if not possibel returns an error
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        # Skip first line
        next(file)
        for line in file:
            line = line.strip().split(",")
            shoe_list.append(Shoe(line[0], line[1], line[2], float(line[3]), int(line[4])))

# Capture shoes enables a user to add a new shoe to the existing inventory returned from the file
def capture_shoes():
    country = input("Enter the country for the shoe: ")
    code = input("Enter the code for the shoe: ")
    product = input("Enter the product name for the shoe: ")
    cost = input("Enter the cost of the shoe: ")
    quantity = input("Enter the quantity of shoes: ")
    
    
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    
    print("\nShoe successfully added to the list.\n")

# View all enables a user to return a data frame with all available inventory items
def view_all(shoe_list):
    
    table = []
    headers = ['country', 'code', 'product', 'cost', 'quantity']
    
    table = pd.DataFrame(shoe.__dict__ for shoe in shoe_list).reindex(columns = headers)
    
    print("\nCurrent Inventory\n")
    print(table)
    
#Re-stok enables a user to update the quantity for the item with the lowest quantity in stock
def re_stock(shoe_list):
    
        # Find shoe with the lowest quantity
    min_quantity = float("inf")
    min_index = -1
    for i, shoe in enumerate(shoe_list):
        if shoe.quantity < min_quantity:
            min_quantity = shoe.quantity
            min_index = i

    # Ask to update the quantity
    if min_index >= 0:
        shoe = shoe_list[min_index]
        add_quantity = int(input("Do you want to add more shoes for {} {}? Enter additional quantity: ".format(shoe.code, shoe.product)))
        shoe.quantity += add_quantity

        # Update file
        with open("inventory.txt", "r") as file:
            data = file.readlines()
        data[min_index + 1] = "{},{},{},{},{}\n".format(shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity)
        with open("inventory.txt", "w") as file:
            file.writelines(data)

# Search shoe enables a user to look up a particular shoe from the inventory
def seach_shoe(shoes_list, shoe_code):
    for shoe in shoe_list:
        try:
            if shoe_code == shoe.code:
                print(f"\n{shoe}\n")
        except:
            print("\nShoe not found.\n")

# Value per item returnd a data frame with the overall value in stock for each product
def value_per_item(shoe_list):
    table = []
    headers = ['country', 'code', 'product', 'total value']
    
    table = pd.DataFrame(shoe.__dict__ for shoe in shoe_list)
    
    table["total value"] = table.cost * table.quantity
    
    print("\nTotal Value per Item\n")
    print(table.reindex(columns = headers))

# Highest quantity returned the item with the highest stock and shows as for sale
def highest_qty(shoe_list):
    
    max_quantity = max(shoe.quantity for shoe in shoe_list)
    for shoe in shoe_list:
        if shoe.quantity == max_quantity:
            print("\nThe product with the highest quantity is for sale:\n{}\n{}\n".format(shoe.code, shoe.product))
    

#==========Main Menu=============
try:
    read_shoes_data()
except FileNotFoundError:
    print( "Error: File not found\n\nPlease ensure inventory.txt file is available.")
    menu_option = "e"
except:
    print( "Error: Unable to read data from file\n\nPlease ensure inventory.txt file is available and in the correct format.")
    menu_option = "e"
    
#This is the menu the user will be prompted with to enter choice
while menu_option != "e":
    menu_option = input(f"""
    
    Enter one of the below functions:
    C - Capture Shoes
    V - View All
    R - Re-stock
    S - Search Shoe
    I- Value per Item
    H - Highest Quanity
    E - Exit
    
    : """).lower()

    # Read Unread emails
    if menu_option == "c":
        capture_shoes()
        
    elif menu_option == "v":
        view_all(shoe_list)
        
    elif menu_option == "r":
        re_stock(shoe_list)
        
    elif menu_option == "s":
        shoe_code = input("Enter shoe code: ")
        seach_shoe(shoe_list, shoe_code)
        
    elif menu_option == "i":
        value_per_item(shoe_list)
        
    elif menu_option == "h":
        highest_qty(shoe_list)
        
    # Exit the program
    elif menu_option == "e":
        print("\nThank you, goodbye.")
        break
    
    # Any other entry is invalid to loop back through menu
    else:
        print("\nIncorrect entry, try again.")