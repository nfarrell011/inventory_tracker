'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Inventory List Class
    This file contains the implementation of Inventory_List class
'''
# import classes to use in the Inventory Class
from inventory_item_class import Inventory_Item
from order_list_class import Order_List
from recipe_class import Recipe_Item

class Inventory_List:
    '''
        Class: Inventory_Item
        Attributes: list_name, inventory_list
        Metheds: add_to_list, ordered, str
    '''
    
    def __init__(self, name: str):
        ''' 
            Constructor: creates a new instance of Inventory List
            Parameters: name, the name of the inventory list, i.e., bar
        '''
        # raise error when argument is not a string
        if not isinstance(name, str):
            raise TypeError("name argument must be data type string.")

        # assign name argument to list.name
        self.list_name = name

        # initiate set and assign to inventory list, this will remove potential duplicates
        self.inventory_list = []

        # create instance of Order_List and assign it to order_list attribute
        self.order_list = Order_List()

    def add_to_list(self, new_item: Inventory_Item):
        ''' 
            Method: add_to_list
            Parameters: name_item, an instance of Inventory_Item
            Returns: none
        '''
        # raise error if argument is not an instance Inventory_Item class
        if not isinstance(new_item, Inventory_Item):
            raise TypeError("new_item must be Inventory_Item object.")

        # add item to inventory set
        if self.inventory_list == []:
            self.inventory_list.append(new_item)
            return
        
        # this checks if item is already in the list, if it is the method will terminate
        for i in range(len(self.inventory_list)):
            if self.inventory_list[i].name == new_item.name:
                return
            
        # if item is not in the list already it will be added
        self.inventory_list.append(new_item)
            
    def ordered(self, item_ordered: Recipe_Item, amount_ordered):
        ''' 
            Method: ordered
            Parameters: 1 Recipe_Item, the item ordered; 1 int, the amount ordered 
            Returns: none
            This method removes the amount of ingredient of the recipe item from the
                corresponding item in the inventory list. It also updates the order list,
                if necessary.
        '''
        # raise errors if arguments are invalid types/values
        if not isinstance(item_ordered, Recipe_Item):
            raise TypeError("item_ordered must be a Recipe_Item object.")
        if not isinstance(amount_ordered, int):
            raise TypeError("amount_ordered must be an integer data type.")
        if amount_ordered <= 0:
            raise ValueError("amount_ordered must be positive integer.")
        
        # this goes through the recipe dictionary
        for i in item_ordered.recipe:
            
            # this iterates through the inventory_list
            for j in range(len(self.inventory_list)):

                # if the recipe item matches the inventory item
                if i == self.inventory_list[j].name:

                    # iterate over the amount ordered
                    for k in range(amount_ordered):

                        # remove the amount from the recipe from the inventory at each 
                        self.inventory_list[j].contains = self.inventory_list[j].contains - item_ordered.recipe[i]

                        # check if the container is empty
                        if self.inventory_list[j].contains < 0:

                            # invoke remove which will remove container from inventory
                            self.inventory_list[j].remove()

                            # invoke open container which will add the amount of a container to contains attribute
                            self.inventory_list[j].open_container()

                            # check if par level has been reached
                            if self.inventory_list[j].containers_held == self.inventory_list[j].par:

                                # if yes, add item to the order list
                                self.order_list.add_to_order_list(self.inventory_list[j])
                            
                            # check if the restuarant has run out of containers
                            elif self.inventory_list[j].containers_held <= 0:
                                
                                # if yes, add item to the order list
                                self.order_list.order_list[self.inventory_list[j].name] += self.inventory_list[j].par

                            # if neither condition above is true, continue
                            else:
                                continue
                        else:
                            continue
                            
    def __str__(self):
        ''' 
            Method: str; turns scoop into a string
            Parameter: self
            Return: a string representation
        '''

        return "Inventory List: " + str(self.list_name) + " contains" + str(self.inventory_list) 
