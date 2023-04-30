'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Inventory Item Class
    This file contains the implementation of Inventory_Item class
'''
class Inventory_Item:
    '''
        Class: Inventory_Item
        Attributes: name, container_size, contains, containers_held, par
        Metheds: open_container, remove, place order, str
    '''
    def __init__(self, name, par, container_size):
        '''
            Constructor: creates an instance of Inventory_Item
            Parameters: self, name, par, container_size
            Creates an instance of class Inventory_Item
        '''
        # check for possible errors with data entry
        if not isinstance(name, str):
            raise TypeError("name must be data type string.")
        if not isinstance(par, int):
            raise TypeError("par must be data type integer.")
        if not isinstance(container_size, float):
            raise TypeError("container_size must be data type float.")
        if par < 0:
            raise ValueError("par must a positve integer.")
        if container_size < 0:
            raise ValueError("container must be a positive integer.")

        # assign name to equal name 
        self.name = name

        # assign container_size equal to container_size to add amount to conatains 
        # when a new container is opened
        self.container_size = container_size

        # assign contains eqaul to container_size
        self.contains = container_size

        # set the amount held to be twice the par, minus the one opened
        self.containers_held = (par * 2) - 1

        # set par to equal par, the amount that will trigger adding item to the order list
        self.par = par

    def open_container(self):
        '''
            Method: open_container
            Parameters: none
            Returns: none
            If there is a container in inventory, this function will open it and
                add the contants to the contains attribute
        '''
        # check if there is a container in inventory to open
        if self.containers_held > 0:

            # if yes, add contents to contains attribute
            self.contains += self.container_size
        else:
            return

    def remove(self):
        '''
            Method: remove
            Parameters: none
            Returns: none
            Removes one container from inventory
        '''
        # if there is a container left in inventory
        if self.containers_held > 0:
            self.containers_held -= 1
        else:
            return

    def place_order(self, amount_ordered):
        '''
            Method: place_order
            Parameters: 1 integer
            Returns: none
                Adds the amount ordered to the containers_held
        '''
        # add amount ordered to the containers_held
        self.containers_held += amount_ordered 

    def __str__(self):
        ''' 
            Method: str; turns scoop into a string
            Parameter: self
            Return: a string representation
        '''
        return "Item: " + str(self.name) + " The container holds " + str(self.container_size) + " amount. We have " + \
            str(self.containers_held) + " currently. We must order at level " + str(self.par) + "\n"
