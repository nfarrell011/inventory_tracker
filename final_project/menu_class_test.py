'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Menu Class
    Imports from menu_class.py and tests the Menu Class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes and methods to test Menu Class
from menu_class import Menu
from recipe_class import Recipe_Item
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # this creates a Menu object to test
        test_menu = Menu("bar_menu")

        # test that name assigns correctly
        self.assertEqual(test_menu.name, "bar_menu")

        # test that the menu list has initiated correctly
        self.assertEqual(test_menu.menu, [])

        # test that menu attribute is a list
        self.assertIsInstance(test_menu.menu, list)

        # this tests that an error is raised when name argument is not a string
        with self.assertRaises(TypeError):
            Menu(3)

    # test add_item method
    def test_add_item(self):

        # create Menu Item and Recipe Items to run tests
        test_menu = Menu("bar")
        item_1 = Recipe_Item("gin", 13.95)
        item_2 = Recipe_Item("vodka", 13.95)

        # invoke add_item method
        test_menu.add_item(item_1)
        test_menu.add_item(item_2)

        # test that the menu has updated correctly
        self.assertEqual(test_menu.menu[0].name, "gin")
        self.assertEqual(test_menu.menu[1].name, "vodka")

        # this tests if a TypeError is raised when name is not a string   
        with self.assertRaises(TypeError):
            test_menu.add_item(1)
        with self.assertRaises(TypeError):
            test_menu.add_item("string")
        with self.assertRaises(TypeError):
            test_menu.add_item(1.1)

        # test that the same item cannot be added to the menu
        test_menu.add_item(item_2)
        print(test_menu.menu)
        self.assertEqual(len(test_menu.menu), 2)

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases
    
# call main function   
if __name__ == "__main__":
    main()