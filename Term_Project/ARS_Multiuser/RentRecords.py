# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Jacob Sunia       #
# @author Sterling Engle           #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

#importing tabulate to ensure that our tables look neat
from tabulate import tabulate


#rentRecords class will represent as our list class that holds all rent records from a specified user
# this classes main purpose will serve as an add new rent records and display feature for output
class RentRecords:
    # The __init__ function is our overloaded constructor that will serve to initialize all of our
    # used items needed in the class. This function runs in a complexity of T(n) = θ(1) based on
    # initialization
    # @param __rentRecord is the list of rent records from the year.
    # @parm __tenantList is the list of tenants that will be used to identify a tenant
    def __init__(self, __rentRecord, __tenantList):
        self.__rows = __rentRecord  # RentRecords dictionary
        self.__tenantList = __tenantList
        self.__months = \
            ['Ap.No', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # insertRent function serves to add onto the current value of the rent function. We would like
    # to implement a new function that clears all values of a rental list but will try to implement
    # if we do have time. The complexity of this algorithm is T(n) = θ(1) based on the use of getting
    # a specified index which is passed in as a parameter
    # @param rent_record will be the record that is passed into the class
    # @param user_login_idx is the login index of the user which we would like to access
    # @param ten_idx is the tenants index that we are set to access in our rent records
    def insertRent(self, rent_record, user_login_idx, ten_idx):
        name, month, amount = rent_record.getInfo()
        self.__rows[user_login_idx][ten_idx][month] += amount
    
    # printable dictionary is our function used to return a list by merging an apartment number to
    # the first index of our rental lists to tabulate in classes further. This function runs in a 
    # runtime of T(n) = O(n) based off of the number of iterations we take into consideration in our
    # function. 
    # @param user_login_idx is the login index of the user which we would like to access
    # @return a list of apartment number and rental lists
    def printable_Dictionary(self, user_login_idx):
        aptNo = []
        # print(self.__tenantList)

        for i in self.__tenantList[user_login_idx]:
            aptNo.append([i['aptNumber']])

        for i in aptNo:
            index = aptNo.index(i)
            i.extend(self.__rows[user_login_idx][index])
        return(aptNo)

    # getSumOfRents is a function that iterates till we get the total of all months and all users in
    # in our function. This function runs in a time complexity of T(n) = O(n^3) based on the number of
    # iterations we are in our 3-Dimensional list
    # @return a rounded number with set precision 2 of our rent total
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
        return round(rTotal,2)

    # display is a function that tabulates our results from printable dictionary. This function is used
    # to simply display all tenant apartment numbers and their respective rent records. The time complexity
    # used to run this function is approximately T(n) = O(n) based on the time it taks for us to create a 
    # printable object
    # @param user_login_idx is the login index of the user which we would like to access
    def display(self, user_login_idx):
        printable = self.printable_Dictionary(user_login_idx)
        print("\n==== Rent Summary =====")
        print(tabulate(printable, headers=self.__months))
        print('Total Rent Collected: $', self.getSumOfRents())
