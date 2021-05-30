# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Jacob Sunia              #
# @author Sterling Engle           #
# @author Matthew Chung            #
# @author Larry Delgado            #
# Due TBD at 23:59PST              #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to Sof Engr #
# Professor Phuyong Nguyen         #
####################################
"""

# import time
import argparse  # command-line parsing library
# import json
# import string
# import re  # regular expressions


# if logFile is defined also logs messages to the log file
def printlog(s):
    print(s)
    if logFile is not None:
        print(s, file=logFile)


# The apartment class stores every instance of a Tenate into our class. It is
# simply an array of Tenant objects in the apartment building
class Apartment:

    # init function is the default constructor(A.K.A the place where all of our
    # Tenant objects are stored) This constructor runs in a time complexity of
    # T(n) = Θ(1) based on initialization of our tenants list.
    # @param tenants_list is the list of our objects
    # @param monthly_expenses is the list of expense objects
    def __init__(self):
        self.tenant_list = []
        self.monthly_expenses = []

    # add tenant function stores our new tenant into our apartment bookings.
    # It is simple a append function for our program to store new objects into
    # our apartment. This function runs in a time complexity of T(n) = Θ(1)
    # based off of our append to the back of our array @param tenant is the new
    # tenate that will be stored into our apartment
    def add_tenant(self, tenant):
        if tenant not in self.tenant_list:
            self.tenant_list.append(tenant)

    # remove tenant function is used to remove a tenant from our apartment
    # list. The time complexity of our remove function runs in T(n) = O(n)
    # based off our iteration through the tenant list @param name is the name
    # of the tenant we are bound to remove
    def remove_tenant(self, name):
        for i in self.tenant_list:
            if i.Name == name:
                self.tenant_list.remove(i)

    # add expenses function adds newly created expenses to our list of expenses
    # paid and reports the specific day, month, category, payee, and amount
    # from the LandLord(John Nguyen). The time complexity of this function runs
    # in T(n) = Θ(1) based on the simple append to our list of expenses
    # this list is not sorted and all based off of what is recorded at that
    # moment in time.
    # @param expense is the expense object that will be defined depending on
    # our users input.
    def add_expenses(self, expense):
        self.monthly_expenses.append(expense)


# tenant class assists our apartment class which the objects
# will be appended to our apartment list
class Tenant:

    # init function is the overloaded constructor for our class
    # @param Name is the name of our tenant
    # @param Apart_No is an integer that will determine our apartment Number
    def __init__(self, Name, Apart_No):
        self.Name = Name
        self.Apart_No = Apart_No
        # an list of 12 zero elements(12 representing No. of months in a year)
        self.payment_list = [0] * 11

    # record_payment function will be our transaction amount that will be
    # recorded in our bookings. All information stored will be directed by
    # our user
    # @param index is the month that we will store our amount at
    # @param amount is the amount of money that will be stored at given index
    def record_payment(self, index, amount):
        self.payment_list.insert(index, amount)

    # print_rental_income will be like a _toString_ function when we print out
    # the monthly payments for each person in the bookings. Its main priority
    # is to print each persons apartment number and rental income as follows.
    # This function runs in a time complexity of T(n) = Θ(1) such that we are\
    # only printing out the payment list and apartment number
    def print_rental_income(self):
        # Prints as follows(Apartment Number-> print list separate by n spaces)
        print(self.Apart_No, *self.payment_list, sep=" ")


# Expenses class will be our object that holds information on each expense. The
# whole purpose of this class is to keep all categories that belong under an
# expense into an instance. That will eventually be stored in our Apartments
# monthly expenses list of items
class Expenses:

    # __init__ function is our overloaded constructor and serves the purpose of
    # creating an object for the expenses class. The whole focus here is to
    # keep all information linked for future use. The time complexity of this
    # function runs in a time of T(n) = Θ(1) because we are only defining what
    # an expense consists of:
    # @param month represents the month which the payment was made on
    # @param day represents the day which the payment was made on
    # @param category represents the category which the payment follows under
    # @param payee represents the person/company/firm/etc. which the payment
    # was paid to @param amount is the transaction amount that will be sent
    # to our payee
    def __init__(self, month, day, category, payee, amount):
        self.month = month
        self.day = day
        self.category = category
        self.payee = payee
        self.amount = amount


def main():
    # argument parser
    ap = argparse.ArgumentParser()
    # ap.add_argument("-j", "--json", type=open, default='AptRentalSys.json',
    #                help="JSON file path")
    ap.add_argument("-o", "--output", type=argparse.FileType('a'),
                    help="log output file path")
    # ap.add_argument("-s", "--skip", type=int, default=0,
    #                help="number of questions to skip")
    args = vars(ap.parse_args())
    global logFile  # output file for printlog(s)
    logFile = args['output']  # optional output file used by printlog(s)
    printlog("Apartment Management System version 0.1")
    printlog("Team 6: Jacob Sunia, Sterling Engle, Matthew Chung, and "
             "Larry Delgado")
    printlog("")

    apa = Apartment()
    tn = Tenant("Jacob", 343)
    apa.add_tenant(tn)
    tn1 = Tenant("Mike", 322)
    apa.add_tenant(tn1)
    tn2 = Tenant("George", 199)
    apa.add_tenant(tn2)

    for i in apa.tenant_list:
        print(i.Name, i.Apart_No)
    # tn = tenant("Jacob",343)
    # ex = Expenses(1, 2, "Insurance", "All State", 4840.0)
    # month = 1
    # tn.record_payment(month-1,1200)

    # print("Apt No Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
    # tn.print_rental_income()
    # print(tn.Name)
    # print(ex.month,"/",ex.day, ex.category, ex.payee, ex.amount)

    # for i in tn.payment_list:
    #     print(i)


if __name__ == "__main__":
    main()
