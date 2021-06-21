# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Matthew Chung     #
# @author Jacob Sunia              #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: June 19, 2021          #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""
from RentRow import RentRow
from RentRecords import RentRecords

class RentInputScreen:  # rental input screen
    def __init__(self, rent_list, tenant_list):
        self.__Name = None
        self.__month = -1
        self.__idx = -1
        self.__amount = 0
        self.__rent_list = rent_list
        self.__tenant_list = tenant_list

    def getRent(self):
        return(self.__Name, self.__month, self.__amount)

    def getIndex(self, login_idx):
        for i, dic in enumerate(self.__tenant_list[login_idx]):
            if dic['name'] == self.__Name:
                self.__idx = i
            

    def inputRent(self, login_idx):
        flag = False
        self.__Name = input('Enter a Tenant Name to Add Payment: ')
        x = 0

        for i in self.__tenant_list[login_idx]:
            if self.__Name in i['name']:
                x = 1
                break
        if x == 0:
            self.inputRent(login_idx)
        self.getIndex(login_idx)
        
        while (self.__month < 0) or (self.__month > 11):
            try:
                print('Months range from (1-12)')
                self.__month = int(input('Please Select a Month Number:'))
                self.__month = self.__month - 1
                if (self.__month > 11) or (self.__month < 0):
                    print('Invalid Month Number, Try again')
                    self.__month = -1
            except:
                print('Invalid Entry, Try Again...')
                self.__month = -1
            
        while flag == False:
            try:
                self.__amount = float(input('Please Enter an Amount you want to Add:'))
                print('Amount: $',self.__amount)
                ays = input('Is this the Correct amount (Y/N):')
                if ays.lower() == 'y':
                    flag = True
            except:
                return(self.__rent_list)
        rentRow = RentRow(self.__Name, self.__month, self.__amount)
        rentRecord = RentRecords(self.__rent_list, self.__tenant_list)
        rentRecord.insertRent(rentRow, login_idx, self.__idx)

        return(self.__rent_list)
