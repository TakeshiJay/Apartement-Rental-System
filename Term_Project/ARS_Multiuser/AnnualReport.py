  
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
# @author Jacob Sunia              #
# @author Sterling Engle           #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

# import tabulate
from ExpenseRecords import ExpenseRecords
from RentRecords import RentRecords


# Initialize class records from previous into 1 Annual Report instance
class AnnualReport:
    # __init__ constructor for self report 1 and 2
    # @param __expenseRecords
    # @param __rentRecords
    # @param __tenant_list 
    def __init__(self, __expenseRecords, __rentRecords, tenant_list):
        self.__report1 = ExpenseRecords(__expenseRecords)
        self.__report2 = RentRecords(__rentRecords, tenant_list)
    
    # calc_netProfit is a function that returns netProfit
    # @return netProfit profit 
    def calc_netProfit(self):
        netProfit = self.__report2.getSumOfRents() - self.__report1.return_total_expenses()
        return netProfit

    # displayAnnualSummary is a function that prints annual summary from inputted information
    def displayAnnualSummary(self):
        print("Annual Summary\n")
        rent_tot = self.__report2.getSumOfRents()
        expe_tot = self.__report1.return_total_expenses()

        print('Income')
        print('Rent Total: $', rent_tot)
        print(" ")
        print('Expense Total: $', expe_tot)
        # Net Profit
        print("\nNet Profit: " + str(self.calc_netProfit()))
