'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Restaurant Class
    This file contains the implementation of Restaurant class
'''
# import classes to use in the Inventory Class
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
from recipe_class import Recipe_Item
from menu_class import Menu
from inventory_list_class import Inventory_List
from random import randint

class Restaurant:
    '''
        Class: Restuarant Class
        Attributes: name, res_menu, res_inventory, sales, income
        Metheds: add_to_list, ordered, str
    '''
    
    def __init__(self, name, menu: Menu, inventory_list: Inventory_List):
        '''
            Constructor: creates an instance of Restaurant Class
            Parameters: self, name, menu:
            Creates an instance of class recipe item
        '''
        # this will raise errors when arguments are not the correct type
        if not isinstance(name, str):
            raise TypeError("name must be data type string")
        if not isinstance(inventory_list, Inventory_List):
            raise TypeError("inventory_list must be data type Inventory List")
        if not isinstance(menu, Menu):
            raise TypeError("menu must be data type Menu")
        
        # assign the initial values to the attributes
        self.name = name
        self.res_menu = menu
        self.res_inventory = inventory_list
        self.sales = {}
        self.income = 0

    def day(self, patrons: int):
        '''
            Method: day
            Parameters: self, patrtons, int; number of people that will be used in simulation
            Returns: nothing
            This method will simulate the orders and sales of restaurant and generate outputs per the 
                number of patrons
        '''
        # raise errors when type and value are invalid
        if not isinstance(patrons, int):
            raise TypeError("patrons must be an integer data type")
        if patrons <= 0:
            raise ValueError("patrans must be a postive integer")
        
        # this iterates over the number of patrons
        for i in range(patrons):

            # generates a random number between 0 and the length of the menu list
            item_index = randint(0, len(self.res_menu.menu) - 1)

            # invoke ordered method, use the menu idex to identify the item
            self.res_inventory.ordered(self.res_menu.menu[item_index], 1)

            # add the price of the item to income attribute
            self.income += self.res_menu.menu[item_index].price

            # check if the item sold is in the sales dictionary 
            if self.res_menu.menu[item_index].name in self.sales:

                # if it is, add on the sold tally
                self.sales[self.res_menu.menu[item_index].name]= self.sales[self.res_menu.menu[item_index].name] + 1

            # if it is not, add to the sales dictionary with a value of 1
            else:
                self.sales[self.res_menu.menu[item_index].name] = 1
