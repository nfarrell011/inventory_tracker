'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Menu Class
    This file contains the implementation of Menu class
'''
from recipe_class import Recipe_Item

class Menu:
    '''
        Class: menu
        Attributes: name, str; menu, dict
        Methods: add_ingredient
    '''
    def __init__(self, name):
        '''
            Constructor: creates an instance of menu_item
            Parameters: self. item_name
            Creates an instance of class recipe item
        '''
        # raise error when argument is not a string
        if not isinstance(name, str):
            raise TypeError("name argument must be data type string.")
        
        # set the initial values of the attributes
        self.name = name
        self.menu = []

    def add_item(self, item: Recipe_Item):
        ''' 
            Method: add_item
            Parameter: self, item, Recipe Item
            Adds a Recipe Item to the restuarant menu attribute
        '''
        # raise error when argument is not a Recipe Item
        if not isinstance(item, Recipe_Item):
            raise TypeError("item argument must be data type Recipe Item.")

        # if the list is empty the item will automattically be added to it
        if self.menu == []:
            self.menu.append(item)
            return

        # this checks if the item is already in the list
        for i in range(len(self.menu)):

            # if it is, the method will terminate
            if self.menu[i].name == item.name:
                return 
            
        # if list is checked and there are duplicates, the item is added to the list
        self.menu.append(item)
                
    def __str__(self):
        ''' 
            Method: str; turns menu into a string
            Parameter: self
            Return: a string representation
        '''
        item_name_list = []
        for i in range(len(self.menu)):
            item_name_list.append(self.menu[i].name)
        return "Menu: " + str(self.name) + " contains: " + str(item_name_list) + " items.\n"
    

