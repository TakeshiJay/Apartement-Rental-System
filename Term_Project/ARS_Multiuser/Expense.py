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

# from ExpenseInputScreen import ExpenseInputScreen


class Expense:
    def __init__(self, year, month, day, category, payee, amount):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__category = category
        self.__payee = payee
        self.__amount = amount

    # getExpense is a function that returns expense information inputted
    # @return __year, __month, __day, __category, __payee, __amount
    def getExpense(self):
        return(self.__year, self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    # validation is a function to pass 
    def validation(self):
        pass
