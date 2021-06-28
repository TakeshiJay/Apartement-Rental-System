# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
#        @author Jacob Sunia       #
#        @author Sterling Engle    #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

from ExpenseInputScreen import ExpenseInputScreen


# Expense(year=2021, month=6)
class Expense:
    def __init__(self, *args, **kwargs):  # required args, then keyword args
        self.__year = 2021
        self.__month = -1
        self.__day = -1
        self.__category = ""
        self.__payee = ""
        self.__amount = ""
        print('args: ', args, ' keyword args: ', kwargs)
        if kwargs.get('month') is None:
            eis = ExpenseInputScreen.inputExpense()
            self.__month, self.__day, self.__category, self.__payee,
            self.__amount = eis.getExpense()
        else:
            self.__year = kwargs.get("year")
            if self.__year is None:
                self.__year = 2021
                self.__month = kwargs.get("month")
                self.__day = kwargs.get("day")
                self.__category = kwargs.get("category")
                self.__payee = kwargs.get("payee")
                self.__amount = kwargs.get("amount")

    # we use a single get to return everything
    def getExpense(self):
        return self.__year, self.__month, self.__day, self.__category, \
            self.__payee, self.__amount

    def get_month(self):
        return(self.__month)

    def get_category(self):
        return(self.__category)

    def get_payee(self):
        return(self.__payee)

    def get_amount(self):
        return(self.__amount)
