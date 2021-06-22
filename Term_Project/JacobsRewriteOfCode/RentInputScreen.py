# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# co-owner: @author Jacob Sunia    #
# co-owner: @author Jacob Sunia    #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: June 21, 2021          #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""
import re  # Regular Expression library


from RentRow import RentRow
from RentRecords import RentRecords


class RentInputScreen:  # rental input screen
    def __init__(self, rent_list, tenant_list):
        self.__Name = None
        self.__month = -1
        self.__tenantIndex = -1
        self.__amount = 0.00
        self.__rent_list = rent_list
        self.__tenant_list = tenant_list

    def getRent(self):
        return(self.__Name, self.__month, self.__amount)

    def setTenantIndex(self, login_idx):
        for i, dic in enumerate(self.__tenant_list[login_idx]):
            if dic['name'] == self.__Name:
                self.__tenantIndex = i

    def getIndex(self, login_idx):
        for i, dic in enumerate(self.__tenant_list[login_idx]):
            if dic['name'] == self.__Name:
                self.__tenantIndex = i

    def inputRent(self, login_idx):
        while self.__Name is None or self.__Name == "":
            self.__Name = input("Enter rent payment tenant name: ")
            if self.__Name == "":
                return self.__rent_list
            validTenant = False
            for tl in self.__tenant_list[login_idx]:
                if self.__Name in tl['name']:
                    validTenant = True
                    break
            if validTenant is False:
                print(f'Invalid tenant name "{self.__Name}"')
                self.__Name = ""
                continue
            else:
                self.setTenantIndex(login_idx)

        # robust month digit collection
        while (self.__month < 0) or (self.__month > 11):
            monthStr = input("Enter payment month (1-12): ")
            if monthStr == "":
                return self.__rent_list
            elif monthStr.isnumeric() is False:
                print(f'Invalid month "{monthStr}", please try again (1-12)')
                continue
            else:
                self.__month = int(monthStr) - 1  # index [0]
                if (self.__month > 11) or (self.__month < 0):
                    print(f'Invalid month {self.__month}, please '
                          'try again (1-12)')
                    self.__month = -1

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                  "Sep", "Oct", "Nov", "Dec"]

        # robust amount ####.## collection
        while self.__amount == 0:
            amountStr = input(f"Enter {months[self.__month]}. payment "
                              f"for {self.__Name}: ")
            if amountStr == "":  # if amount string is empty return
                return self.__rent_list
            # TODO force 0-2 digits after decimal point using regular exp.
            # elif re.match(r'^-?\d+(?:\.\d+)$', amountStr) is None:
            elif re.match(r'^-?\d+(?:\.?\d+)$', amountStr) is None:
                print(f'Invalid amount "{amountStr}", please enter dollars '
                      "and cents (250.42) with no $")
                self.__amount = 0.00
                continue
            else:
                self.__amount = float(amountStr)
                rentRow = RentRow(self.__Name, self.__month, self.__amount)
                rentRecord = RentRecords(self.__rent_list, self.__tenant_list)
                rentRecord.insertRent(rentRow, login_idx, self.__tenantIndex)
                if self.__amount >= 0:
                    print(f'${self.__amount:0.2f} {months[self.__month]}. '
                          f'rent payment recorded for {self.__Name}')
                else:
                    print(f'${self.__amount:0.2f} {months[self.__month]}. '
                          "security deposit return recorded "
                          f"for {self.__Name}")
        return self.__rent_list
