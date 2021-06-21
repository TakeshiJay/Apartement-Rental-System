import tabulate
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
from RentRow import RentRow 

class RentRecords:
    def __init__(self, __rentRecord, __tenantList):
        self.__rows = __rentRecord  # RentRecords dictionary
        self.__tenantList = __tenantList
        self.__months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        
    def insertRent(self, rent_record, user_login_idx, ten_idx):
        name, month, amount = rent_record.getInfo()
        self.__rows[user_login_idx][ten_idx][month] = amount


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
        print("\n==== Rent Summary =====")
        # Tabulate
        for i in self.__months:
            print(i, end='\t\t')
        print()

        # for i in self.__rows[user_login_idx]:
        #     for j in i:
        #         aligned_j = "{:<5}".format(j)
        #         print(aligned_j, end='\t')
        #     print()
        # print()
        for i in range(len(self.__rows[user_login_idx])):
            print(self.__rows[user_login_idx][i])

        # headers = self.__rows[user_login_idx].keys()
        # rows = [x.values() for x in self.__rows[user_login_idx]]
        # print(tabulate.tabulate(rows, headers, tablefmt='rst'))

        # headers = self.__rows.keys()
        # rows = [x.values() for x in self.__rows]
        # print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        
        # Print Rent Total Last
        # print(f"\nRent Total: ${self.getSumOfRents():.2f}")
