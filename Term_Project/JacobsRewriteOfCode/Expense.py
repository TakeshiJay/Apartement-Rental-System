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

from ExpenseInputScreen import ExpenseInputScreen


class Expense:
    def __init__(self):
        eis = ExpenseInputScreen.inputExpense()
        self.__month, self.__day, self.__category, self.__payee,
        self.__amount = eis.getExpense()

    # FIXME  we use a single get to return everything
    def get_month(self):
        return(self.__month)

    def get_category(self):
        return(self.__category)

    def get_payee(self):
        return(self.__payee)

    def get_amount(self):
        return(self.__amount)
