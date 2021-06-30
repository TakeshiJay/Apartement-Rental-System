# -*- coding: utf-8 -*-
"""
########## Term Project ##################
#                                        #
# rewritten by:  @author Sterling Engle  #
# owner:         @author Larry Delgado   #
# prototyped by: @author Jacob Sunia     #
#                                        #
# Due Jun 24, 2021 at 11:59 PM PDT       #
# Finished: TBD at TBD                   #
#----------------------------------------#
# CSULB CECS 343 Intro to S/W Engr       #
# Professor Phuong Nguyen                #
##########################################
"""

import datetime
import tabulate
from Expense import Expense


class ExpenseRecords:
    # __init__ copies existing expense dictionary to a list of Expense,
    # if any
    # @param expenseRecord
    def __init__(self, expenseRecord):
        self.__thisYear = datetime.datetime.now().year
        self.__newExpense = None
        self.__updatedList = []
        self.__map = ['Year', 'Month', 'Day', 'Category', 'Payee', 'Amount']

        if len(expenseRecord) > 0 and type(expenseRecord[0]) is dict:
            self.__expenseList = []  # store as a list for this landlord
            for entry in expenseRecord:
                self.__updatedList.append(Expense(entry.get("Year"),
                                                  entry.get("Month"),
                                                  entry.get("Day"),
                                                  entry.get("Category"),
                                                  entry.get("Payee"),
                                                  entry.get("Amount")))
        else:
            self.__updatedList = expenseRecord

    # getExpenseDict returns the expense records as a dictionary
    def getExpenseDict(self):
        expenseDictList = []
        for expense in self.__updatedList:
            eDict = {}  # expense dictionary list entry
            eDict["Year"], eDict["Month"], eDict["Day"], eDict["Category"], \
                eDict["Payee"], eDict["Amount"] = expense.getExpense()

            expenseDictList.append(eDict)
        return expenseDictList

    # keep expenses sorted by year, month, day ascending
    def sortExpenses(self, order=0):
        if order == 0:  # ascending by date
            self.__updatedList.sort(key=lambda e: e.getEpochDay())  # in place
        else:  # ascending by category
            self.__updatedList.sort(key=lambda e: e.getCategory())  # in place

    # insertExp is a function that fills in dictionary
    # @param expenseRecord
    def insertExp(self, expenseRecord):
        year, month, day, category, payee, amount = expenseRecord.getExpense()

        self.__newExpense = Expense(year, month, day, category, payee, amount)
        self.__updatedList.append(self.__newExpense)
        # keep expenses sorted by year, month, day ascending
        self.sortExpenses()

    def displayExpenseYearCategories(self, year):
        cat = ""
        expSum = 0.00

        print("Expenses:")
        if len(self.__updatedList) == 0:
            print("  None recorded for this period.")
            return
        for e in self.__updatedList:
            if e.getCategory() != cat:
                if expSum != 0:
                    print(f"  {cat:20s} ${expSum:10.2f}")
                cat = e.getCategory()
                expSum = e.getAmount()
            else:
                expSum += e.getAmount()
        if cat != "" and expSum != 0:
            print(f"  {cat:20s} ${expSum:10.2f}")

    # return_total_expenses is a function that returns total expenses
    # @return sum
    def return_total_expenses(self, year=0):  # year 0 returns all years
        sum = 0.0
        for e in self.__updatedList:
            if year == 0 or year == e.getYear():
                sum += e.getAmount()
        return sum

    # displaySummary is a function that prints total expenses
    def displaySummary(self):
        if len(self.__updatedList) < 1:
            print("\nNo expense records to display.\n")
            return
        print("\n                 ==== Expense Summary ====\n")
        # Tabulate
        headers = ["Year", "Month", "Day", "Category", "Payee", "Amount"]
        rows = [e.getExpense() for e in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        # Print Expense Total Last
        print("Total Expenses:                                "
              f"${self.return_total_expenses():8.2f}")
