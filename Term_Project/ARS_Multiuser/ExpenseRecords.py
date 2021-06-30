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
    # __init__ initialize expenses with empty dictionary and updates as needed
    # @param expenseRecord
    def __init__(self, expenseRecord):
        self.__expenses = {}
        self.__updatedList = expenseRecord
        self.__map = ['Year', 'Month', 'Day', 'Category', 'Payee', 'Amount']

    # insertExp is a function that fills in dictionary
    # @param expenseRecord 
    def insertExp(self, expenseRecord):
        year, month, day, category, payee, amount = expenseRecord.getExpense()
        self.__expenses['Year'] = year
        self.__expenses['Month'] = month
        self.__expenses['Day'] = day
        self.__expenses['Category'] = category
        self.__expenses['Payee'] = payee
        self.__expenses['Amount'] = amount
        self.__updatedList.append(self.__expenses)

    # return_total_expenses is a function that returns total expenses 
    # @return sum 
    def return_total_expenses(self):
        sum = 0.0
        for i in self.__updatedList:
            sum += i['Amount']
        return sum

    # displaySummary is a function that prints total expenses 
    def displaySummary(self):
        if len(self.__updatedList) < 1:
            print("\nNo expense records to display.\n")
            return
        print("\n                 ==== Expense Summary ====\n")
        # Tabulate
        headers = self.__updatedList[0].keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        # Print Expense Total Last
        print(f"Total Expenses: ${self.return_total_expenses():0.2f}")

    def displayCatExp(self):
        catSum = 0
        print("Category Expense Sub-Total")
        print("======== =================")
        copiedList = []
        '''
        for i in self.__updatedList:
            if i['Category'] == i-1['Category']:
                catSum = catSum + i-1['Amount']
            else:
                print(f"{i['Category']},    {i['Amount']}")
        for i in self.__updatedList:
                if i['Category'] == i-1['Category']:
                '''
                    
