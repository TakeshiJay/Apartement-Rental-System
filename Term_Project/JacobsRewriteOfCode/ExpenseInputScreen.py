
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
# @author Jacob Sunia              #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""
from Expense import Expense
from ExpenseRecords import ExpenseRecords

class ExpenseInputScreen:  # Expense input screen
    def __init__(self, expense_list):
        self.__month = -1
        self.__day = -1
        self.__category = None
        self.__payee = None
        self.__amount = 0.00
        self.__expense_list = expense_list

    def getExpense(self):
        return(self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    def inputExpense(self):
        hiddenMonth = 0
        while (self.__month < 0) or (self.__month > 11):
            monthStr = input("Enter a month (1-12): ")
            if monthStr == "":
                return self.__month
            elif monthStr.isnumeric() is False:
                print(f'Invalid month "{monthStr}", please try again (1-12)')
                continue
            else:
                self.month = int(monthStr) - 1  #[0]
                if (self.month > 11) or (self.month < 0):
                    print(f'Invalid month {self.month}, please '
                          'try again (1-12)')
                    self.month = -1
            hiddenMonth = self.__month

        while (self.__day < 0) or (self.__day > 29):
            if (hiddenMonth == 2):
                dayStr = input("Enter a day value(1-28): ")
            else:
                dayStr = input('Please Enter a Day Value(1-31): ')

            if dayStr == "":
                return self.__day
            elif dayStr.isnumeric() is False:
                print(f'Invalid day "{dayStr}", please try again (1-28)')
                continue
            elif(self.__day > 27 and hiddenMonth==2):
                self.__day = -1
                print(f'Invalid day "{dayStr}", please try again')
                continue
      
        self.__category = input('Enter Expense Category(Repairing, Utilities):')
        self.__payee = input('Enter payee (Bob\'s Hardware, Big Electric Co):')

        while self.__amount == 0:
            amountStr = input('Enter amount(39.95):')
            if amountStr == "":
                return self.__amount #empty
            elif re.match(r'^-?\d+(?:\.?\d+)$', amountStr) is None:
                print("Invalid input, please do not use $")
                self.__amount = 0.00
                continue
            else:
                self.__amount = float(amountStr) #convert amount to float
        expense = Expense(self.__month, self.__day, self.__category, self.__payee, self.__amount)
        expenseRecord = ExpenseRecords(self.__expense_list)
        expenseRecord.insertExp(expense)
