  
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Sterling Engle    #
# @author Jacob Sunia              #
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
<<<<<<< HEAD
    def __init__(self, expenseRecords, rentRecords):
        print("expenseRecords")
        print(expenseRecords)
        print("rentRecords:")
        print(rentRecords)
        self.__report1 = ExpenseRecords(expenseRecords)
        self.__report2 = RentRecords(rentRecords)
=======
    def __init__(self, __expenseRecords, __rentRecords, tenant_list):
        self.__report1 = ExpenseRecords(__expenseRecords)
        self.__report2 = RentRecords(__rentRecords, tenant_list)
>>>>>>> 35044c44725cdb68f505a420ebe81fd4d365ccf2

    def calc_netProfit(self):
        netProfit = self.__report2.getSumOfRents() - self.__report1.return_total_expenses()
        return netProfit

    # The whole annual summary
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
