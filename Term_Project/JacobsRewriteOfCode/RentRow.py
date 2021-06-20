# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Matthew Chung     #
# @author Jacob Sunia              #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

# TODO  REMOVE THIS!
from RentInputScreen import RentInputScreen


class RentRow:
    def __init__(self):
        ris = RentInputScreen.inputRentPayment()
        self.__name, self.__month, self.__amount = ris.inputRentPayment()

    def get_name(self):
        return(self.__name)

    def get_month(self):
        return(self.__month)

    def get_amount(self):
        return(self.__amount)
