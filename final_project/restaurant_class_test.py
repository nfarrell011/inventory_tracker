'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Restaurant Class
    Imports from restaurant_class.py and tests the Restaurant class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes to use in the Restaurant Class tests
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
from recipe_class import Recipe_Item
from menu_class import Menu
from inventory_list_class import Inventory_List
from random import randint
from restaurant_class import Restaurant
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # create objects to runs tests
        res_item_1 = Recipe_Item("gin", 10.00)
        res_item_2 = Recipe_Item("vodka", 10.00)
        inven_item_1 = Inventory_Item("gin", 3, 3.0)
        inven_item_2 = Inventory_Item("vodka", 4, 4.00)
        menu = Menu("bar")
        inven_list = Inventory_List("bar_inven")
        menu.add_item(res_item_1)
        menu.add_item(res_item_2)
        inven_list.add_to_list(inven_item_1)
        inven_list.add_to_list(inven_item_2)

        # create instance of restaurant
        restaurant = Restaurant("Dave's", menu, inven_list)

        # test the attributes values
        self.assertEqual(restaurant.name, "Dave's")
        self.assertEqual(len(restaurant.res_menu.menu), 2)
        self.assertEqual(restaurant.res_menu.menu[0].name, "gin")
        self.assertEqual(restaurant.res_menu.menu[1].name, "vodka")
        self.assertEqual(restaurant.sales, {})
        self.assertEqual(restaurant.income, 0)
        self.assertEqual(len(restaurant.res_inventory.inventory_list), 2)
        self.assertEqual(restaurant.res_inventory.inventory_list[0].name, "gin")
        self.assertEqual(restaurant.res_inventory.inventory_list[1].name, "vodka")

        # test the errors
        with self.assertRaises(TypeError):
            Restaurant("Dave's", "string", inven_list)
        with self.assertRaises(TypeError):
            Restaurant("Dave's", menu, "string")
        with self.assertRaises(TypeError):
            Restaurant(3, menu, inven_list)
        with self.assertRaises(TypeError):
            Restaurant("Dave's", menu, 3.0)

    def test_day(self):

        # create objects to runs tests
        res_item_1 = Recipe_Item("gin", 10.00)
        res_item_2 = Recipe_Item("vodka", 10.00)
        inven_item_1 = Inventory_Item("gin", 3, 3.0)
        inven_item_2 = Inventory_Item("vodka", 4, 4.0)
        menu = Menu("bar")
        inven_list = Inventory_List("bar_inven")
        menu.add_item(res_item_1)
        menu.add_item(res_item_2)
        inven_list.add_to_list(inven_item_1)
        inven_list.add_to_list(inven_item_2)

        # create instance of restaurant
        restaurant = Restaurant("Dave's", menu, inven_list)

        # invoke day method with 4 as argument
        restaurant.day(4)

        # test that associated values are updated properly
        self.assertEqual(restaurant.income, 40.00)
        self.assertEqual(sum(restaurant.sales.values()), 4)

        # test the errors
        with self.assertRaises(TypeError):
            restaurant.day("string")
        with self.assertRaises(TypeError):
            restaurant.day(4.55)
        with self.assertRaises(ValueError):
            restaurant.day(-1)

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases

# call main function   
if __name__ == "__main__":
    main()