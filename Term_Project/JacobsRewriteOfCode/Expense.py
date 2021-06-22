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
    def __init__(self, year, month,day,category,payee):
        eis = ExpenseInputScreen().inputExpense()
        self.__year = year
        self.__month= month
        self.__day =day
        self.__category = category
        self.__payee = payee
        self.__amount = eis.getExpense()

    def getRent(self):
        return(self.__month, self.__category, self.__payee, self.__amount)

    def validation(self):
        pass
