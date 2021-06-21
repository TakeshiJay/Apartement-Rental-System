from tabulate import tabulate
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Matthew Chung            #
# @author Sterling Engle           #
# @author Jacob Sunia              #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

class RentRecords:
    def __init__(self, __rentRecord, __tenantList):
        self.__rows = __rentRecord  # RentRecords dictionary
        self.__tenantList = __tenantList
        self.__months = ['Ap.No','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
    def insertRent(self, rent_record, user_login_idx, ten_idx):
        name, month, amount = rent_record.getInfo()
        self.__rows[user_login_idx][ten_idx][month] += amount

    def printable_Dictionary(self, user_login_idx):
        aptNo = []
        
        for i in self.__tenantList:
            aptNo.append([i['aptNumber']])
        for i in aptNo:
            index = aptNo.index(i)
            i.extend(self.__rows[user_login_idx][index])
        return(aptNo)        


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
    def display(self, user_login_idx):
        printable = self.printable_Dictionary(user_login_idx)
        print("\n==== Rent Summary =====")
        print(tabulate(printable,headers=self.__months))
        print('Total Rent Collected: $',self.getSumOfRents())
        print()
