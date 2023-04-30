'''
    Joseph Nelson Farrell
    CS 5001
    03/22/2023
    Create Report Function
    This file contains the function that will generate a pdf output file.
        It will create the plots, add the plots to the pdf. It will also add an order
        list to the pdf.
'''
# import classes to use in the Restaurant Class tests
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
from restaurant_class import Restaurant

def create_report(restaurant):
    '''
        Function: create_report
        Parameters: 1 Restaurant object
        Returns: nothing; 
            This function generates a PDF file containing matplotlib plots, and summery
            information.
    '''
    # raise an error if argument is not Restaurant object
    if not isinstance(restaurant, Restaurant):
        raise TypeError("restaurant must be a Restaurant Object.")
    
    # this inherits from FPDF class and creates new class PDF with additional methods
    class PDF(FPDF):
        def header(self):
            self.image('restaurant-icon-png-4874.png', 10, 8, 25)
            self.set_font('Arial', "I", 8)
            self.cell(0, 10, "Report Generated on: " + str(datetime.now()), border = False, ln = 1, align = "R" )
            self.ln(20)
        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f'Page {self.page_no()}', align="C")
    
    # create an instance of PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "BIU", size = 16)
    pdf.cell(0, 10, txt = "Sales & Inventory Report: " + str(restaurant.name), ln = 1, align = "C")
    pdf.set_font("Arial", "I", size = 12)
    pdf.cell(0, 10, txt = "Gross Revenue: " + "$" + str(round(restaurant.income, 2)), ln = 1, align = "L")
    pdf.set_font("Arial", "IU", size = 12)
    pdf.cell(50, 10, txt = "Items and Amounts That Need to be Ordered", ln = 1, align = "L")
    pdf.set_font("Arial", size = 12)
    for item in restaurant.res_inventory.order_list.order_list:
        pdf.cell(50, 10, txt = item + ": " + str(restaurant.res_inventory.order_list.order_list[item]).capitalize(), ln = 1, align = "L", border=True)

    # create bar graph of items sold and add it to pdf
    names = list(restaurant.sales.keys())
    values = list(restaurant.sales.values())
    plt.bar(range(len(restaurant.sales)), values, tick_label = names)
    plt.xlabel("Items Sold")
    plt.ylabel("Amount Sold")
    plt.title("Indvidual Items Sold")
    plt.xticks(rotation = 45)
    plt.subplots_adjust(bottom = .35)
    pdf.add_page()
    plt.savefig("sales.png")
    pdf.image("sales.png", x = None, y = None, w=140, h = 80, type = '', link = '')
    plt.show()

    # create bar graph of order list and add it to pdf
    names_2 = list(restaurant.res_inventory.order_list.order_list.keys())
    values_2 = list(restaurant.res_inventory.order_list.order_list.values())
    plt.bar(range(len(restaurant.res_inventory.order_list.order_list)), values_2, tick_label = names_2)
    plt.title("Order List")
    plt.xlabel("Items to Order")
    plt.ylabel("Amount Needed")
    plt.xticks(rotation = 60)
    plt.subplots_adjust(bottom = .35)
    plt.savefig("order_list.png")
    pdf.image("order_list.png", x = None, y = None, w=140, h = 80, type = '', link = '')
    pdf.output("report.pdf")
    plt.show()


