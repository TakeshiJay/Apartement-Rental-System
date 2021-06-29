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


class RentRow:
    # __init__ constructor
    # @param name name
    # @param month month
    # @param amount amount
    def __init__(self, name, month, amount):
        #self.__rentRow = {}
        
        self.__name = name
        self.__month = month
        self.__amount = amount

    # get_name function to return name
    # @return __name
    def get_name(self):
        return(self.__name)

    # get_month function returns month
    # @return __month
    def get_month(self):
        return(self.__month)

    # get_amount function returns amount
    # @return __amount
    def get_amount(self):
        return(self.__amount)
    
    # getInfo return info
    # @return __name, __month, __amount
    def getInfo(self):
        return(self.__name, self.__month, self.__amount)
    
    '''
    def getRentSum(self):
        sum = 0.0
        for i in self.__rentRow:
            sum+= i
        return sum
    '''
