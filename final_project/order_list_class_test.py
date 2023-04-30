'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Order_List Class
    Imports from order_list_class.py and tests the Order_List class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes and methods to test Order List Class
from inventory_list_class import Inventory_List
from recipe_class import Recipe_Item
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # create instance of Order_List
        test_list = Order_List()

        # test that the order list was created correctly
        self.assertEqual(test_list.order_list, {})

        # test that order_list attrobute contains an instance of Order_List
        self.assertIsInstance(test_list.order_list, dict)

    # test for the add_to_list method
    def test_add_to_order_list(self):

        # create instance of Order_List
        test_list = Order_List()

        # create Inventory_Items to use in tests
        item_1 = Inventory_Item("gin", 1, 1.0)
        item_2 = Inventory_Item("vodka", 2, 2.0)

        # invoke add_to_list method
        test_list.add_to_order_list(item_1)
        test_list.add_to_order_list(item_2)

        # test that the list updated correctly
        self.assertEqual(test_list.order_list, {'gin': 1, 'vodka': 2})

        # test that the list updates correctly
        test_list.add_to_order_list(item_2)
        self.assertEqual(test_list.order_list, {'gin': 1, 'vodka': 4})

        # this tests if a TypeError is raised when item to order is not an Inventory Item   
        with self.assertRaises(TypeError):
            test_list.add_to_order_list(1)
        with self.assertRaises(TypeError):
            test_list.add_to_order_list("string")
        with self.assertRaises(TypeError):
            test_list.add_to_order_list(1.1)


# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases
    

# call main function   
if __name__ == "__main__":
    main()