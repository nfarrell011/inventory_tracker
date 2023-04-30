'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Helper Functions
    Imports the helper functions from helper_functions.py and tests the functions
        to ensure they are generating the correct lists.
'''
# import classes to use in the tests
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
from recipe_class import Recipe_Item
from menu_class import Menu
from inventory_list_class import Inventory_List
from random import randint
from restaurant_class import Restaurant
import unittest
from helper_functions import read_in_inventory
from helper_functions import read_in_recipe

# define CrashTest to using unitttest TestCase, for read_in_recipe
class CrashTest(unittest.TestCase):

    # test for the read_in_recipe function
    def test_read_in_recipe(self):

        # invoke function, assign return to menu
        menu = read_in_recipe("recipe_1.csv", "dave's")

        # test that the Menu Item has been generated succussfully
        self.assertEqual(len(menu.menu), 17)
        self.assertEqual(menu.name, "dave's")
        self.assertIsInstance(menu, Menu)
        self.assertIsInstance(menu.menu[2], Recipe_Item)
        self.assertIsInstance(menu.menu[0], Recipe_Item)
        self.assertIsInstance(menu.menu[10], Recipe_Item)
    
        # test the errors
        with self.assertRaises(TypeError):
            read_in_recipe(3, "dave's")
        with self.assertRaises(ValueError):
            read_in_recipe("file.txt", "dave's")
        with self.assertRaises(TypeError):
            read_in_recipe("recipe_1.csv", 3)
        with self.assertRaises(FileNotFoundError):
            read_in_recipe("file.csv", "dave's")
    # test for the read_in_recipe function
    def test_read_in_inventory(self):

        # invoke function, assign return to menu
        inventory_list = read_in_inventory("inventory_list_1.csv", "bar")

        # test that the Menu Item has been generated succussfully
        self.assertEqual(len(inventory_list.inventory_list), 27)
        self.assertIsInstance(inventory_list, Inventory_List)
        self.assertIsInstance(inventory_list.inventory_list[2], Inventory_Item)
        self.assertIsInstance(inventory_list.inventory_list[0], Inventory_Item)
        self.assertIsInstance(inventory_list.inventory_list[26], Inventory_Item)
        
        # test the errors
        with self.assertRaises(TypeError):
            read_in_recipe(3, "bar")
        with self.assertRaises(ValueError):
            read_in_recipe("file.txt", "bar")
        with self.assertRaises(TypeError):
            read_in_recipe("inventory_list_1.csv", 3)
        with self.assertRaises(FileNotFoundError):
            read_in_recipe("file.csv", "bar")

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases

# call main function   
if __name__ == "__main__":
    main()