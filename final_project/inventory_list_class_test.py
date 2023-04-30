'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Inventory_List Class
    Imports from inventory_list_class.py and tests the Inventory_List class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes and methods to test Inventory_List Item Class
from inventory_list_class import Inventory_List
from recipe_class import Recipe_Item
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # test that the object is created successfully and that attribute values assign
        # correctly
        test_list = Inventory_List("bar_inventory")

        # test that name assigns correctly
        self.assertEqual(test_list.list_name, "bar_inventory")

        # test that the inventory list has initiated correctly
        self.assertEqual(test_list.inventory_list, [])

        # test that order_list attrobute contains an instance of Order_List
        self.assertIsInstance(test_list.order_list, Order_List)

        # test that the inventory set attribute contains an instance of set
        self.assertIsInstance(test_list.inventory_list, list)

    # test for the add_to_list method
    def test_add_to_list(self):

        # create Inventory_List Object to test
        test_list = Inventory_List("bar_inventory")

        # create Inventory_Items to use in tests
        item_1 = Inventory_Item("gin", 1, 1.0)
        item_2 = Inventory_Item("vodka", 2, 2.0)

        # invoke add_to_list method
        test_list.add_to_list(item_1)
        test_list.add_to_list(item_2)
        test_list.add_to_list(item_2)

        # test that item_1 and item_2 were added to the test_list
        self.assertEqual(len(test_list.inventory_list), 2)

        # test that item_1 and item_2 were added to the test_list
        self.assertEqual(len(test_list.inventory_list), 2)

        # test the errors
        with self.assertRaises(TypeError):
            test_list.add_to_list("string")
        with self.assertRaises(TypeError):
            test_list.add_to_list(67)
        with self.assertRaises(TypeError):
            test_list.add_to_list(3.45)
    
    # test for the ordered method
    def test_ordered(self):

        # create Inventory_List Object to test
        test_list = Inventory_List("bar_inventory")

        # create Inventory_Items to use in tests
        item_1 = Inventory_Item("gin", 2, 2.0)
        item_2 = Inventory_Item("vodka", 3, 2.0)

        # invoke add_to_list method, to create active list
        test_list.add_to_list(item_1)
        test_list.add_to_list(item_2)
        print(test_list.inventory_list)

        # create recipe item that uses inventory item
        recipe_item = Recipe_Item("vodka_tonic", 13.95)
        recipe_item.add_ingredient("vodka", 2)

        # create second recipe item to run additional tests
        recipe_item_2 = Recipe_Item("gin & tonic", 13.95)
        recipe_item_2.add_ingredient("gin", 1)

        # invoke ordered method
        test_list.ordered(recipe_item, 4)

        # test that a container_held was removed when a container became empty
        self.assertEqual(test_list.inventory_list[1].containers_held, 2)

        # test that inventory_item is added to order list when containers_held get below par
        self.assertEqual(len(test_list.order_list.order_list), 1)
        self.assertEqual(test_list.order_list.order_list[item_2.name], 3)
        self.assertEqual(test_list.order_list.order_list, {'vodka': 3})

        # invoke ordered method
        test_list.ordered(recipe_item_2, 4)

        # test that a container_held was removed when a container became empty
        self.assertEqual(test_list.inventory_list[1].containers_held, 2)

        # test that inventory_item is added to order list when containers_held get below par
        self.assertEqual(len(test_list.order_list.order_list), 2)
        self.assertEqual(test_list.order_list.order_list[item_2.name], 3)
        self.assertEqual(test_list.order_list.order_list, {'vodka': 3, 'gin': 2})

    # second test for the ordered method and associated attributes
    def test_ordered(self):

        # create Inventory_List Object to test
        test_list = Inventory_List("bar_inventory")

        # create Inventory_Items to use in tests
        item_1 = Inventory_Item("bourbon", 3, 6.0)

        # invoke add_to_list method, to create active list
        test_list.add_to_list(item_1)
        self.assertEqual(test_list.inventory_list[0].containers_held, 5)
        self.assertEqual(test_list.inventory_list[0].par, 3)
        self.assertEqual(test_list.inventory_list[0].contains, 6)
        self.assertEqual(test_list.inventory_list[0].container_size, 6)

        # create recipe item that uses inventory item
        recipe_item = Recipe_Item("bourbon_up", 13.95)
        recipe_item.add_ingredient("bourbon", 3.0)

        # invoke ordered method
        test_list.ordered(recipe_item, 6)

        # test that a container_held was removed when a container became empty
        self.assertEqual(test_list.inventory_list[0].containers_held, 3)
        self.assertEqual(test_list.inventory_list[0].par, 3)
        self.assertEqual(test_list.inventory_list[0].contains, 0)
        self.assertEqual(test_list.inventory_list[0].container_size, 6)

        # test that inventory_item is added to order list when containers_held get below par
        self.assertEqual(len(test_list.order_list.order_list), 1)
        self.assertEqual(test_list.order_list.order_list[item_1.name], 3)
        self.assertEqual(test_list.order_list.order_list, {'bourbon': 3})

        # test the errors
        with self.assertRaises(TypeError):
            test_list.ordered("string", 4)
        with self.assertRaises(TypeError):
            test_list.ordered(item_1, 4)
        with self.assertRaises(TypeError):
            test_list.ordered(5.5, 4)
        with self.assertRaises(TypeError):
            test_list.ordered(recipe_item, "4")
        with self.assertRaises(TypeError):
            test_list.ordered(recipe_item, 4.4)
        with self.assertRaises(ValueError):
            test_list.ordered(recipe_item, 0)

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases
    
# call main function   
if __name__ == "__main__":
    main()