
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
#        @author Jacob Sunia       #
#        @author Sterling Engle    #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""
import datetime  # for getting the current year
import re
from Expense import Expense


class ExpenseInputScreen:  # Expense input screen
    # __init__ initializer
    # @param expense_list  this is a list of dictionary
    def __init__(self, expense_list):
        self.__year = datetime.datetime.now().year
        self.__month = datetime.datetime.now().month
        self.__nowDay = datetime.datetime.now().day
        self.__day = self.__nowDay
        self.__category = None
        self.__payee = None
        self.__amount = 0.00
        self.__expense_list = expense_list

    # getExpense is a function that returns expense information
    # @return __year, __month, __day, __category, __payee, __amount
    def getExpense(self):
        return(self.__year, self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    # inputExpense is a function that takes in expense input
    # @return __expenseList
    def inputExpense(self):
        while True:
            yearStr = input(f"Enter expense year (default {self.__year}): ")
            if yearStr == "":
                break
            elif yearStr.isnumeric() is False:
                print(f'Invalid year "{yearStr}", please try again')
                continue
            else:
                self.__year = int(yearStr)  # [0]
                if (self.__year < 2021):
                    print(f'Invalid year {self.__year}, please '
                          'try again it must be 2021 or later')
                    self.__year = 2021
                    continue
                break

        while True:
            monthStr = input(f"Enter expense month (default {self.__month}): ")
            if monthStr == "":
                hiddenMonth = self.__month
                break  # accept default today's month
            elif monthStr.isnumeric() is False:
                print(f'Invalid month "{monthStr}", please try again (1-12)')
                self.__month = datetime.datetime.now().month
                continue
            else:
                self.__month = int(monthStr)
                if (self.__month > 12) or (self.__month < 1):
                    print(f'Invalid month {self.__month}, please '
                          'try again (1-12)')
                    self.__month = datetime.datetime.now().month
                    continue
                else:
                    hiddenMonth = self.__month
                    break
            hiddenMonth = self.__month


        while True:
            if (hiddenMonth == 2):
                dayStr = input("Enter expense day (1-28): ")
            else:
                dayStr = input('Enter expense day (1-31): ')

            if dayStr == "":
                return self.__expense_list
            elif dayStr.isnumeric() is False:
                print(f'Invalid day "{dayStr}", please try again (1-28)')
                continue
            elif self.__day > 27 and hiddenMonth == 2:
                self.__day = -1
                print(f'Invalid day "{dayStr}", please try again')
                continue
            else:
                self.__day = int(dayStr)
                break

        self.__category = \
            input('Enter expense category(e.g. repairs, utilities): ')
        self.__payee = input('Enter payee (Bob\'s Hardware, Big Electric Co):')

        while self.__amount == 0:
            amountStr = input('Enter amount (39.95):')
            if amountStr == "":
                return self.__expense_list  # empty
            elif re.match(r'^-?\d+(?:\.?\d+)$', amountStr) is None:
                print('Invalid input "{amountStr}", please do not use $')
                self.__amount = 0.00
                continue
            else:
                self.__amount = float(amountStr)  # convert amount to float
        expense = Expense(self.__year, self.__month, self.__day,
                          self.__category, self.__payee, self.__amount)
        # expenseRecord = ExpenseRecords(self.__expense_list)
        self.__expense_list.insertExp(expense)
        return self.__expense_list
