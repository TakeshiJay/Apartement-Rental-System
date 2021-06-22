# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
#        @author Jacob Sunia       #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

import tabulate


class ExpenseRecords:
    # Initialize expenses with empty dictionary and updates as needed
    def __init__(self, expenseRecord):
        self.__expenses = {}
        self.__updatedList = expenseRecord
        self.__map = ['Year','Month','Day','Category','Payee','Amount']

    def insertExp(self, expenseRecord):
        year, month, day, category, payee, amount = expenseRecord.getExpense()
        self.__expenses['Year'] = year
        self.__expenses['Month'] = month
        self.__expenses['Day'] = day
        self.__expenses['Category'] = category
        self.__expenses['Payee'] = payee
        self.__expenses['Amount'] = amount
        self.__updatedList.append(self.__expenses)

    # If key is 'Amount' add the value of it to eTotal
    def return_total_expenses(self):
        sum = 0.0
        for i in self.__updatedList:
            sum += i['Amount']
        return sum   

    # Print Expense Records
    def displaySummary(self):
        print(self.__updatedList)
        print("==== Expense Summary ====")
        # Tabulate
        headers = self.__updatedList[0].keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        # Print Expense Total Last
        # print("\nExpense Total: " + str(self.return_total_expenses()))
        print('Total Expense: $',self.return_total_expenses())
