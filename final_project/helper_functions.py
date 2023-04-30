'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Helper Functions
    This file contains the helper functions for the application file.
        The read in function for the inventory list
        The read function for recipe
'''
# import classes and packages
from inventory_item_class import Inventory_Item
from inventory_list_class import Inventory_List
from menu_class import Menu
from recipe_class import Recipe_Item
import csv
import os

def read_in_recipe(recipe_file, menu_name):
    '''
        Function: read_in_recipe
        Parameters: 1, a csv file
        Returns: 1 instance of Menu; 
            This function reads in the csv file containing the menu and the recipe.
            It creates multiple instances Recipe Item and adds all the Recipe Items 
            to a single instance of Menu  
    '''
    # raise errors when values/types are not correct
    # raise error if inventory does not contain .csv
    if ".csv" not in (recipe_file):
        raise ValueError("inventory_file must be a csv file")
    if not isinstance(recipe_file, str):
        raise TypeError("inventory_file must be a string data type.")
    if not isinstance(menu_name, str):
        raise TypeError("inventory_name must be a string data type.")
    if not os.path.isfile(recipe_file):
        raise FileNotFoundError("inventory_file cannot be found, check the file name and location.")
    
    # assign the file to a variable
    input_1 = recipe_file

    # open the csv file with the read argument
    with open(input_1, "r") as recipe_file:

        # invoke csv.reader function and save the csv file as recipe_csv
        recipe_cvs = csv.reader(recipe_file)

        # this skips the first row
        next(recipe_cvs)

        # initialize a list to hold the recipe items once they are created
        item_list = []

        # the tracker variable will be used to add the ingredients to the correct Recipe Item
        tracker = -1

        # go through the csv file, line by line
        for row in recipe_cvs:

            # if column one is empty it indicates a new item needs to be created
            if row[1] == '':

                # update tracker
                tracker += 1

                # create instance of Recipe Item
                item_list.append(Recipe_Item(row[0], float(row[3])))

            # if column one is not empty, it indicates that the row contains ingredients of the 
            # preceding Recipe Item    
            elif row[1] != '':

                # this adds the ingredients to the Recipe Item
                item_list[tracker].add_ingredient(row[1], float(row[2]))

    # create an instance of Menu            
    menu_name = Menu(menu_name)

    # iterate through the generated list of recipe items
    for i in range(len(item_list)):

        # add each item to the Menu
        menu_name.add_item(item_list[i])

    # return the Menu
    return menu_name

def read_in_inventory(inventory_file, inventory_name):
    '''
        Function: read_in_inventory
        Parameters: 1, a csv file
        Returns: 1 instance of Inventory List; 
            This function reads in the csv file containing the inventory list.
            It creates multiple instances Inventory Item and adds all the Inventory Items 
            to a single instance of Inventory List  
    '''
    # raise errors when values/types are not correct
    # raise error if inventory does not contain .csv
    # raise file not found error if the file is not in the directory
    if ".csv" not in (inventory_file):
        raise ValueError("inventory_file must be a csv file")
    if not isinstance(inventory_file, str):
        raise TypeError("inventory_file must be a string data type.")
    if not isinstance(inventory_name, str):
        raise TypeError("inventory_name must be a string data type.")
    if not os.path.isfile(inventory_file):
        raise FileNotFoundError("inventory_file cannot be found, check the file name and location.")
    
    # assign the file to a variable
    input = inventory_file

    # open the csv file with the read argument
    with open(input, "r") as inven_file:

        # invoke csv.reader function and save the csv file as inventory_csv
        inventory_csv = csv.reader(inven_file)

        # skip the first row
        next(inventory_csv)

        # initailize an empty list
        item_list_2 = []

         # go through the csv file, line by line
        for row in inventory_csv:

            # invoke Inventory Item and create an new instance of Inventory Item for each row
            item_list_2.append(Inventory_Item(row[0], int(row[2]), float(row[1])))

    # invoke Inventory List, create an instance of inventory list        
    kitchen_inventory = Inventory_List(inventory_name)

    # iterate through the generated list of Inventory Items
    for i in range(len(item_list_2)):

        # add each item to the Inventory List object
        kitchen_inventory.add_to_list(item_list_2[i])

    # return one instance of Inventory List
    return kitchen_inventory

