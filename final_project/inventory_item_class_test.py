'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Inventory_Item Class
    Imports from inventory_item_class.py and tests the Inventory_Item class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes and methods to execute test
from inventory_item_class import Inventory_Item
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # this creates a inventory_item to test
        item = Inventory_Item("eggs", 6, 12.0)

        # this tests that the name has assigns correctly
        self.assertEqual(item.name, "eggs")

        # this tests that the par has assigns correctly
        self.assertEqual(item.par, 6)

        # this tests that containers_held assigns correctly
        self.assertEqual(item.containers_held, 11)

        # this tests that contains assigns correctly
        self.assertEqual(item.contains, 12.0)

        # this tests that container_size assigns correctly
        self.assertEqual(item.container_size, 12.0)

        # this tests if a TypeError is raised when name is not a string   
        with self.assertRaises(TypeError):
            Inventory_Item(1, 1, 1.0)

        # this tests if a TypeError is raised if par is not an integer
        with self.assertRaises(TypeError):
            Inventory_Item("eggs", "1", 1.0)

        # this tests if a TypeError is raised container_size is not an flaot
        with self.assertRaises(TypeError):
            Inventory_Item("curry", 1, "1")

        # this test if a ValueError is raised when container_size is negative
        with self.assertRaises(ValueError):
            Inventory_Item("eggs", 1, -1.0)

        # this test if a ValueError is raised when par is negative
        with self.assertRaises(ValueError):
            Inventory_Item("eggs", -1, 1.0)
    
    # this will test if add_ingredient is functioning correctly
    def test_open_container(self):

        # create an inventory item to test
        item = Inventory_Item("eggs", 1, 4.0)
    
        # invoke open_container method
        item.open_container()

        # this tests if the contains has the correct amount 
        self.assertEqual(item.contains, 8.0)

    # this will test if add_ingredient is functioning correctly
    def test_remove(self):

        # create an inventory item to test
        item = Inventory_Item("eggs", 4, 4.0)
    
        # invoke remove method
        item.remove()

        # this tests if the containers_held has the correct amount 
        self.assertEqual(item.containers_held, 6)

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases
    

# call main function   
if __name__ == "__main__":
    main()