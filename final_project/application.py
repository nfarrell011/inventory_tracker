'''
    Joseph Nelson Farrell
    CS 5001
    04/17/2023
    Applications
    This file contains the application that will create an instance of Restaurant Class
        simulate n number of people incoming to the restaurant
'''
# import classes to use in the Restaurant Class tests
from restaurant_class import Restaurant
from helper_functions import read_in_inventory
from helper_functions import read_in_recipe
from pdf_function import create_report

##############____________________MAIN_____________________#################
def main():
    '''
        Function: main
        Parameters: none
        Returns: none 
            This is where simulation is executed
    '''
    try:
        # get user inputs, file names, etc., to set up simulation
        inventory_file = input("What is the of your inventory file?\n")
        inventory_name = input("What is the name of inventoy list?\n")
        menu_file = input("What is the name of your menu file?\n")
        menu_name = input("What is the name of your menu?\n")
        restaurant_name = input("What is your restaurant's name?\n")

        # set covers to equal 0 to use as loop variable in asking permission with repitition
        covers = 0

        # this loop will execute while covers is less than zero
        while covers <= 0:

            # retrieve number of covers from user
            covers = input("How many covers would you like to simulate?\n")

            # check if value entered by user is numeric
            if covers.isnumeric():

                # if covers is numeric, convert to integer and assign to covers variable
                covers = int(covers)
            
            # if covers is not numeric, inform user that covers must be a positive integer
            else:
                covers = 0
                print("Covers must be a positive integer.\n")

        # invoke read_inventory function, read in file, create objects
        read_inventory = read_in_inventory(inventory_file, inventory_name)

        # invoke read_menu funtion, read in file, create objects
        read_menu = read_in_recipe(menu_file, menu_name)

        # invoke Restaurant class, create Restuarant Class
        restaurant_name = Restaurant(restaurant_name, read_menu, read_inventory)

        # invoke day() method to run simulation
        restaurant_name.day(covers)

        # invoke create_report to generate pdf output with values stored in Restaurant object
        create_report(restaurant_name)
        
    except TypeError as ex:
        print("Invalid type:", type(ex), ex)
    except ValueError as ex:
        print("Invalid value:", type(ex), ex)
    except FileNotFoundError as ex:
        print("File not found:", type(ex), ex)

# main function   
if __name__ == "__main__":
    main()




