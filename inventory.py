#import pythons table formet
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # This function, you must initialise the following attributes:
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity     
        
    def get_cost(self):
        #Add the code to return the cost of the shoe in this method.
        return self.cost

    def get_quantity(self):
        #Add the code to return the quantity of the shoes.
        return self.quantity

    def __str__(self):
        #Add a code to returns a string representation of a class.
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()
        # create a new get code function
    def get_code(self):
        return self.code

#=============Shoe list===========

#The list will be used to store a list of objects of shoes.
items_list = []
shoe_list = []

#==========Functions outside the class==============

   # This function will open the file inventory.txt
   # and read the data from this file, then create a shoes object with this data
   # and append this object into the shoes list. One line in this file represents
   # data to create one object of shoes. You must use the try-except in this function
   # for error handling. Remember to skip the first line using your code.

inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")

def read_shoes_data():
    file = None
    try:
        for line in inventory_read:
            str_line = line.strip("\n")
            spl_line = str_line.split(",")
            items_list.append(spl_line)

        for i in range(1, len(items_list)):
            temp = items_list[i]
            shoe1 =  Shoe(temp[0], temp[1], temp[2], temp[3], int(temp[4]))
            shoe_list.append(shoe1)

    except FileNotFoundError as error:
        print("\nThe file you are trying to access does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

   # Use try, except and finally to accout for errors if file doesn't open
   # This function will allow a user to capture data
   # about a shoe and use this data to create a shoe object
   # and append this object inside the shoe list. 

def capture_shoes():
    file = None

    try:
        user_country = input("Please enter the country of your product:\n")
        user_code = input("Please enter the code of your product:\n")
        user_product = input("Please enter the name of your product:\n")
        user_cost = int(input("Please enter the cost of your product, only in numbers. E.g. 12345\n"))
        user_quantity = int(input("Please enter the quantity of your product, only in numbers. E.g. 2\n"))

        new_shoe = Shoe(user_country, user_code, user_product, user_cost, user_quantity)      #create a shoe object 
        shoe_list.append(new_shoe)               # append object to the list of shoes

        inventory_write.write(f'\n{user_country},{user_code},{user_product},{user_cost},{user_quantity}')
        print("\nThank you, your product has been loaded!\n")

        inventory_write.close()

    except FileNotFoundError as error:
        print("\nThe file you are trying to access does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()
    

    # This function will iterate over the shoes list and
    # print the details of the shoes returned from the __str__
    # function. Optional: you can organise your data in a table format
    # by using Python’s tabulate module.

def view_all():
    file = None
    
    try:

        print("\n---------------------------------------------STOCKLIST---------------------------------------------\n")
        #create lists of items for each attribute
        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        for lines in shoe_list:       
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))

        print("\n---------------------------------------------END-------------------------------------------------\n")

    except FileNotFoundError as error:
        print("\nThis file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

    # This function will find the shoe object with the lowest quantity,
    # which is the shoes that need to be re-stocked. Ask the user if they
    # want to add this quantity of shoes and then update it.
    # This quantity should be updated on the file for this shoe.   

def restock():
    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoe_list.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoe_list[i])
    
        print("\n----------------------------Lowest stock items:----------------------------\n")

        for line in restock_list:
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid', showindex= range(1,6)))
        
        print("\n---------------------------------------------------------------------------\n")
        #ask user for index of item and quantity
        input_item = int(input("\nPlease confirm the index of the product you want to restock:\n"))
        input_qty = int(input("\nPlease confirm the new quantity:\n"))
        list[input_item].set_quantity(input_qty)
        #create a empty string to write to
        output = ''
        for item in shoe_list:      #increment the string by cost and quantity(add them to list)
            output += (f'{item.get_cost()},{item.get_quantity()}\n')
        #write to our text file all the added items
        inventory_file = open("inventory.txt", "w")
        inventory_file.write(output)
        inventory_file.close()

        print("\nYour product has been updated!")
    # use try, except and finally block for any file error
    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

    # This function will search for a shoe from the list
    # using the shoe code and return this object so that it will be printed.   

def search_shoe():
    find_shoe = input("\nEnter the code you are searching for:\n\n")

    for line in shoe_list:
        if line.get_code() == find_shoe:
            print(f'\n {line}')

    print("\nChoose another option from the menu below\n")
    
    # This function will calculate the total value for each item.
    # Please keep the formula for value in mind: value = cost * quantity.
    # Print this information on the console for all the shoes.

def value_per_item():
    for line in shoe_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} VALUE PER ITEM: R{value}\n')
    
    # Write code to determine the product with the highest quantity and
    # print this shoe as being for sale.

def highest_quantity():
    print("\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoe_list, key=lambda item: item.quantity))       # use max to get the item with a higher quantity
    print("\nThis item is on sale!\n")
    

# ====================================================== OUTPUT =============================================== #

  

#==========Main Menu=============
# Create a menu that executes each function above.
# This menu should be inside the while loop. Be creative!

# Display menu options
# Use try/finally in case the file does not open on user end
# Set ValueError
read_shoes_data()
while True:

    try:
        menu = int(input('''\n

            Welcome to Nike's Inventory System! 

            Choose an option from the menu below:

            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_quantity()

        elif menu > 6:
            print("\nIncorrect selection. Please try again! Choose from the menu below.\n")

    except ValueError:
        print("\nYour choice is invalid option. Try again, enter a number.\n")
        
# ====================================================== END =============================================== #