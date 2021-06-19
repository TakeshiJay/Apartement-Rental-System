# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Matthew Chung            #
# @author Sterling Engle           #
# @author Jacob Sunia              #
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
        self.__rows = __rentRecord  # RentRecords dictionary

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
        rTotal = 0.00
        # print(self.__rows)
        """
        for key in self.__rows:
            print(key, '->', self.__rows[key])
            rTotal += self.__rows[key]
        """
        for user in self.__rows:
            for name in user:
                for month in name:
                    rTotal += month
        return rTotal

    # Print Rent Record
    def display(self):
        print("\n==== Rent Summary =====")
        # Tabulate
        '''
        headers = self.__Rent_List.keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        '''
        # Print Rent Total Last
        print(f"\nRent Total: ${self.getSumOfRents():.2f}")
