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
import ExpenseRecords
import RentRecords


# Initialize class records from previous into 1 Annual Report instance
class AnnualReport:
    def __init__(self, __expenseRecords, __rentRecords):
        self.__report1 = ExpenseRecords(__expenseRecords)
        self.__report2 = RentRecords(__rentRecords)

    def calc_netProfit(self):
        netProfit = RentRecords.return_total_rents() - \
            ExpenseRecords.return_total_expenses()
        return netProfit

    # The whole annual summary
    def displayAnnualSummary(self):
        print("Annual Summary\n")
        self.__report2.display()
        print(" ")
        self.__report1.displaySummary()
        # Net Profit
        print("\nNet Profit: " + str(self.calc_netProfit()))
