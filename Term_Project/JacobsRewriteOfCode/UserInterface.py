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


from LoginInputScreen import LoginInputScreen
from TenantList import TenantList
from TenantInputScreen import TenantInputScreen
from Expense import Expense
from ExpenseRecords import ExpenseRecords
from RentRow import RentRow
from RentRecords import RentRecords
from UserList import UserList


# JavaScript Object Notation, is an open standard file format and data
# interchange format that uses human-readable text to store and transmit data
# objects consisting of attribute–value pairs and arrays
# (or other serializable values)
import json  # json used to read and write from persistent storage data file
# import time  # time used to delay some processes that we need to slow down


# UserInterface class conains the login and menu process
# @param __dic is the current dictionary that is loaded with all
#              information regarding both the LandLord(s) and their tenants
class UserInterface:  # user interface

    # __init__ default constructor that builds the User Interface. The
    # constructor provides a space to print and prompt the Landlord
    # @param flag boolean indicates if a user is logged in or not
    # @param __expenses_List is an extended list of dictionary expense items
    # @param __loged_user_idx is the current index of the logged in user;
    # initially set to -1 because there are no current logged in users.
    # @param __tenants_list is the list of tenants leasing one of the logged in
    # users' apartments.
    # @param __rent_records is a list of records throughout a yearly cycle
    # that record all tenant payment transactions.
    def __init__(self):
        f = open('login.json', )
        self.__dic = json.load(f)
        self.__UserList = self.__dic["Username"]
        self.__password = self.__dic["Password"]
        self.__expenses_List = self.__dic["Expenses"]
        self.__loged_user_idx = -1
        self.__tenants_list = self.__dic["TenantList"]
        self.__rent_records = self.__dic["RentRecords"]

    def loginMainMenu(self):
        self.print_menus(1)
        if self.logon_menu() is False:
            return False
        self.__tenantList = \
            TenantList(self.__tenants_list[self.__loged_user_idx])
        self.__tenantScreen = TenantInputScreen(self.__tenantList)

        scanner = ''
        while (scanner != 'l'):
            scanner = input("Enter 'i' to Input data, 'd' to Display data, "
                            "or 'l' to Logout: ")
            if scanner.lower() == 'i':
                self.print_menus(3)
                scanner_2 = input("      press [Enter] to return "
                                  "to main menu: ")
                self.inputScreen(scanner_2)
            elif scanner.lower() == 'd':
                self.print_menus(4)
                scanner_2 = input("      press [Enter] to return "
                                  "to main menu: ")
                self.output_screen(scanner_2)
            elif scanner.lower() == 'l':
                print("Thank you for using the Apartment Management System "
                      "by Team 6.")
                print("See you again soon!\n")
                return True
            else:
                print(f'"{scanner}" is an invalid option please try again.')
        return True

    def inputScreen(self, scanner_2):
        if scanner_2 == 't':
            self.__tenants_list[self.__loged_user_idx] = \
                self.__tenantScreen.inputTenant()
            # TODO: convert into format here for JSON storage

            # tenant = Tenant()
            # ten_list = TenantList(self.__tenants_list[self.__loged_user_idx],
            #                       self.__rent_records[self.__loged_user_idx])
            # ten_list.inputTenant(tenant.getTenant(), tenant.getApt())
        #
        elif scanner_2 == 'r':
            rent_row = RentRow()
            rent_list = RentRecords(self.__rent_records, self.__loged_user_idx,
                                    self.__tenants_list[self.__loged_user_idx])
            rent_list.insertRent(rent_row.get_month(),
                                 rent_row.get_amount(),
                                 rent_row.get_name())
            self.rentRecords = rent_list
        #
        elif scanner_2 == 'e':
            expense = Expense()
            expense_List = \
                ExpenseRecords(self.__expenses_List[self.__loged_user_idx])
            expense_List.insertExp(expense.get_month(),
                                   expense.get_day(),
                                   expense.get_category(),
                                   expense.get_payee(),
                                   expense.get_amount())
            expense_List.displaySummary()
            # we should move this line to output_screen
        # TODO remove next line when TenantList converted and handled in here
        if scanner_2 != 't':
            self.store_to_file()

    # Output Screen
    def output_screen(self, scanner_2):
        if scanner_2 == 't':
            tenantList = TenantList(self.__tenants_list)
            tenantList.display()
        elif scanner_2 == 'r':
            rentRecords = RentRecords(self.__rent_records)
            rentRecords.display()
        elif scanner_2 == 'e':
            expenseRecords = ExpenseRecords(self.__expenses_List)
            expenseRecords.displaySummary()
        elif scanner_2 == 'a':
            pass

    def logon_menu(self):
        user = LoginInputScreen()
        userList = UserList(self.__UserList, self.__password,
                            self.__tenants_list, self.__rent_records,
                            self.__expenses_List)

        while userList.flag is False:
            login = input("Enter 1 to login, 2 to create new user, "
                          "or 'q' to Quit: ")
            if login == '1':  # user login
                lis = LoginInputScreen()
                user = lis.inputUser()
                if user is not None:
                    userList.return_user(user)
                    self.__loged_user_idx = userList.get_logged_idx()
            elif login == '2':  # create new user/password and login
                lis = LoginInputScreen()
                user = lis.inputNewUser()
                if user is not None:
                    userList.add_user(user)
                    print('New user logged In...\n')
                    self.store_to_file()
                    self.__loged_user_idx = userList.get_logged_idx()
            elif login.lower() == 'q':  # quit program
                return False
            else:
                print(f'"{login}" is an invalid entry, please try again.')
        return True

    def print_menus(self, num):
        if num == 1:
            print('Welcome to the Apartment Management System v0.3')
            print('Please select one of the following login options:')
        elif num == 3:
            print("\nEnter 't' to add or replace a Tenant,")
            print("      'r' to record a Rent payment,")
            print("      'e' to record an Expense payment, or", end='')
        # For output_screen
        elif num == 4:
            print("\nEnter 't' to display Tenant list,")
            print("      'r' to display Rent records,")
            print("      'e' to display Expense records,")
            print("      'a' to display Annual summary, or", end='')
        else:
            print(f"Menu number {num} not supported.")

    def store_to_file(self):
        js = json.dumps(self.__dic)
        f = open("login.json", "w")
        f.write(js)
        f.close()
