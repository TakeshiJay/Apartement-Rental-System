# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Jacob Sunia              #
# @author Sterling Engle           #
# @author Matthew Chung            #
# @author Larry Delgado            #
#                                  #
# Due TBD at 23:59 PDT             #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""


class RentRecords:
    def __init__(self, __rentRecord):
        self.__rows = __rentRecord

    def insertRent(self, month, amount):
        if month > 0 and month < 13:
            self.__rows[month - 1] = amount
            return True
        else:
            print(f"RentRecords.insertRent(): invalid month {month}")
            return False

    def insertRentRow(self, row):
        print("RentRecords.insertRentRow() not implemented.")
        return False

    # Get Rent Total
    def getSumOfRents(self):
        rTotal = 0
        for key in self.__RentRecord:
            rTotal += self.__rentRecord[key]
        return rTotal

    # Print Rent Record
    def display(self):
        print("==== Rent Summary =====")
        print(self)
        # Tabulate
        '''
        headers = self.__Rent_List.keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        '''
        # Print Rent Total Last
        print("\nRent Total: " + str(self.getSumOfRents()))
