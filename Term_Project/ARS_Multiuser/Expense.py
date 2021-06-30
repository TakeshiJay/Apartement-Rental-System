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

from datetime import date
# from datetime import timedelta

epoch = date(2021, 1, 1)  # date epoch began Jan 1, 2021 before ARS


class Expense:
    def __init__(self, year, month, day, category, payee, amount):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__category = category.lower()
        self.__payee = payee.lower()
        self.__amount = amount

    # getExpense returns all private expense information:
    # @return __year, __month, __day, __category, __payee, __amount
    def getExpense(self):
        return self.__year, self.__month, self.__day, \
               self.__category.capitalize(), self.__payee.title(), \
               self.__amount

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def getDay(self):
        return self.__day

    def getCategory(self):
        return self.__category.capitalize()

    def getPayee(self):
        return self.__payee.title()

    def getAmount(self):
        return self.__amount

    # The "epoch" begins on Jan 1, 2021 which is day number 0 since ARS
    # did not exist then
    def getEpochDay(self):
        expenseDay = date(self.getYear(), self.getMonth(), self.getDay())
        return expenseDay - epoch

    # validation is a function that always passes success now
    def validation(self):
        pass
