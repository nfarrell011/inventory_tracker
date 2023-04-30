'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Recipe Item Class
    This file contains the implementation of Recipe_Item class
'''
class Recipe_Item:
    '''
        Class: recipe_item
        Attributes: name, str; recipe, dict; price, float
        Methods: add_ingredient
    '''
    def __init__(self, item_name, price: float):
        '''
            Constructor: creates an instance of recipe_item
            Parameters: self, item_name, price
            Creates an instance of class recipe item
        '''
        # check for possible errors with data entry
        if not isinstance(price, float):
            raise TypeError("Price must be data type float.")
        if not isinstance(item_name, str):
            raise TypeError("item_name must be data type string.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        
        # set price to equal price
        self.price = price
        
        # set name to equal item_name
        self.name = item_name
        
        # initiate a dictionary to store recipe 
        self.recipe = {}

    def add_ingredient(self, ingredient: str, amount: float):
        ''' 
            Method: add_ingredient
            Parameter: self, 1 str, 1 int; name of ingredient and amount in recipe
            Adds an ingredient to the recipe
        '''
        # check for possible errors with data
        if not isinstance(ingredient, str):
            raise TypeError("Ingredient must be data type string.")
        if not isinstance(amount, float):
            raise TypeError("Amount must be data type float.")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # add item to the dictionary
        self.recipe[ingredient] = amount

    def __str__(self):
        ''' 
            Method: str; turns scoop into a string
            Parameter: self
            Return: a string representation
        '''
        return "Your recipe item is: " + str(self.name) + " with ingredients: " + str(self.recipe) + "\n"