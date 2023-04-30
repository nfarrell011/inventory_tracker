'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Test Suite for Recipe_Item Class
    Imports from recipe_class.py and tests the Recipe_Item class by creating objects,
        calling methods on the objects, and making sure the values match the expected values.
'''
# import classes and methods to test Recipe Item Class
from recipe_class import Recipe_Item
import unittest

# define CrashTest to using unitttest TestCase
class CrashTest(unittest.TestCase):

    # test the constructor and the attributes
    def test_init(self):

        # this creates a carton to test
        item = Recipe_Item("curry", 29.95)

        # this tests that the name has assigned correctly
        self.assertEqual(item.name, "curry")

        # this tests that the price has assigned correctly
        self.assertAlmostEqual(item.price, 29.95)

        # this tests that the recipe dictionary has been initiated
        self.assertEqual(item.recipe, {})

        # this tests if a TypeError is raised when name is not a string   
        with self.assertRaises(TypeError):
            Recipe_Item(-1, 29.95)

        # this tests if a TypeError is raised if price is not a float
        with self.assertRaises(TypeError):
            Recipe_Item("curry", 2)

        # this tests if an ValueError is raised price is not positve
        with self.assertRaises(Exception):
            Recipe_Item("curry", -29.95)
    
    # this will test if add_ingredient is functioning correctly
    def test_add_ingredient(self):

        # create an instance of recipe_item
        item = Recipe_Item("hot dog", 4.00)

        # invoke add_ingredients to recipe
        item.add_ingredient("bun", 1.0)
        item.add_ingredient("hot dog", 1.0)

        # this tests if recipe dictionary contains the correct items and amounts
        self.assertEqual(item.recipe, {'bun': 1.0, 'hot dog': 1.0})

        # this tests if a TypeError is raised when ingredient is not a string
        with self.assertRaises(TypeError):
            item.add_ingredient(95, 4.0)
        
        # this tests if a TypeError is raised when amount is not a float
        with self.assertRaises(TypeError):
            item.add_ingredient("flour", "cat")

        # this tests if a ValueError is raised when amount is not a positive
        with self.assertRaises(ValueError):
            item.add_ingredient("flour", -4.0)

# create main function to run tests 
def main():

    # call unittests built-in main function
    unittest.main(verbosity = 3) # verbosity increases
    

# call main function   
if __name__ == "__main__":
    main()