
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
        self.__amount = None
        self.__expense_list = expense_list

    def getExpense(self):
        return(self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    def inputExpense(self):
        hiddenMonth = 0
      
        while (self.__month < 0) or (self.__month > 11):
            try:
                self.__month = int(input('Please Enter a Month Value (1-12):'))
                hiddenMonth = self.__month
                self.__month -= 1
            except:
                print('Invalid Input, Try again...')

        while (self.__day < 0) or (self.__day > 29):
            try:
                if (hiddenMonth == 2):
                    self.__day = int(input('Please Enter a Day Value(1-28):'))
                    self.__day -= 1
                    if(self.__day > 27):
                        self.__day = -1
                else:
                    self.__day = int(input('Please Enter a Day Value(1-31):'))
                    self.__day -= 1
            except:
                print('Invalid Input, Please Try Again')
                self.__day = -1
        self.__category = input('Enter Expense Category(Repairing, Utilities):')
        self.__payee = input('Enter payee (Bob\'s Hardware, Big Electric Co):')
        self.__amount = float(input('Enter amount(39.95):'))
        expense = Expense(self.__month, self.__day, self.__category, self.__payee, self.__amount)
        expenseRecord = ExpenseRecords(self.__expense_list)
        expenseRecord.insertExp(expense)
