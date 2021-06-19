# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Matthew Chung            #
# @author Sterling Engle           #
# @author Jacob Sunia              #
# @author Larry Delgado            #
#                                  #
# Due TBD at 23:59 PDT             #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

# import tabulate


class ExpenseRecords:
    # Initialize expenses with empty dictionary and updates as needed
    def __init__(self, expenseRecord):
        self.__expenses = {}
        self.__updatedList = expenseRecord

    def insertExp(self, month, day, category, payee, amount):
        self.__expenses['Month'] = month
        self.__expenses['Day'] = day
        self.__expenses['Category'] = category
        self.__expenses['Payee'] = payee
        self.__expenses['Amount'] = amount
        self.__updatedList.append(self.__expenses)

    # If key is 'Amount' add the value of it to eTotal
    def return_total_expenses(self):
        eTotal = 0
        for key in self.__updatedList:
            if key is 'Amount':
                eTotal += self.__updatedList[key]
        return eTotal

    # Print Expense Records
    def displaySummary(self):
        print("==== Expense Summary ====")
        print(self)
        # Tabulate
        '''
        headers = self.__updatedList[0].keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        '''
        # Print Expense Total Last
        print("\nExpense Total: " + str(self.return_total_expenses()))
