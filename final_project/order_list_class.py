'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Order List Class
    This file contains the implementation of Order List class
'''
# import classes and methods from Inventory_Item Class
from inventory_item_class import Inventory_Item

class Order_List:
    '''
        Class: Order List
        Attributes: order_list, a list containers the items that need to be ordered
            and amounts that need to be ordered
        Metheds: add_to_order_list
    '''
    def __init__(self):
        '''
            Constructor: creates an instance of Order List
            Parameters: self
            Creates an instance of of the Order List Class
        '''
        # assign the attribute to an empty dictionary
        self.order_list = {}

    def add_to_order_list(self, item_to_order: Inventory_Item):
        '''
            Method: add_to_order_list
            Parameters: 1 Inventory Item, item to be added to the order list
            Returns: none
            This method will add an Inventory Item to the order list, the name of the item will be the key
                and the value of par attribute will be the value
        '''
        if not isinstance(item_to_order, Inventory_Item):
            raise TypeError("The item must an instance of Inventory_Item.")
        
        # check if the item is in the list already
        if item_to_order.name in self.order_list:

            # if it is, add the value of the par attribute to the existing value
            self.order_list[item_to_order.name] += item_to_order.par
        
        # if it is not in the list, add it to the list
        else:
            self.order_list[item_to_order.name] = item_to_order.par

    def __str__(self):
        ''' 
            Method: str; turns an Order List instance in to a string
            Parameter: self
            Return: a string representation
        '''
        return "The order list contains:" + str(self.order_list)


      