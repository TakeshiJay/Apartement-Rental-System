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

import datetime
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
        self.__thisYear = datetime.datetime.now().year

    # calc_netProfit is a function that returns netProfit
    # @return netProfit profit
    def calc_netProfit(self):
        netProfit = self.__report2.getSumOfRents() - \
            self.__report1.return_total_expenses(self.__thisYear)
        return netProfit
<<<<<<< HEAD

    # displayAnnualSummary is a function that prints annual summary
    # from inputted information
    def displayAnnualSummary(self):
        print("")
        print(f"        {self.__thisYear} Annual Summary")
        print("")
=======
        
    # displayAnnualSummary is a function that prints annual summary from inputted information
    def displayAnnualSummary(self):
        print("Annual Summary\n----------------")
>>>>>>> 5bb3948e52ca0133dbd31cdeff69a946214540dc
        rent_tot = self.__report2.getSumOfRents()

        self.__report1.sortExpenses(1)
        expe_tot = self.__report1.return_total_expenses(self.__thisYear)
        self.__report1.sortExpenses(0)

<<<<<<< HEAD
        print('Income')
        print(f"Rent Total:            ${rent_tot:10.2f}")
        print("")
        self.__report1.displayExpenseYearCategories(self.__thisYear)
        print("")
        print(f"Expense Total:         ${expe_tot:10.2f}")
        # Net Profit
        print("")
        print(f"Net Profit:            ${self.calc_netProfit():10.2f}")
=======
        print('Income\n----------------')
        print('Rent Total: $', rent_tot, '\n----------------')
        cat_exp = self.__report1.displayCatExp()
        print(" ")
        print('Expense Total: $', expe_tot, '\n----------------')
        # Net Profit
        print("\nNet Profit: " + str(self.calc_netProfit()))
            
>>>>>>> 5bb3948e52ca0133dbd31cdeff69a946214540dc
