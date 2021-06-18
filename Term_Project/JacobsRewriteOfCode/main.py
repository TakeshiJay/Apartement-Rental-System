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

from Tenant import Tenant
from TenantList import TenantList
from TenantInputScreen import TenantInputScreen
from USER import User
from Expense import Expense
from ExpenseRecords import ExpenseRecords
from RentRow import RentRow
from RentRecords import RentRecords
from User_List import User_List


# JavaScript Object Notation, is an open standard file format and data
# interchange format that uses human-readable text to store and transmit data
# objects consisting of attribute–value pairs and arrays
# (or other serializable values)
import json  # json used to read and write from persistent storage data file
import time  # time used to delay some processes that we need to slow down


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
        self.__user_list = self.__dic["Username"]
        self.__password = self.__dic["Password"]
        self.__expenses_List = self.__dic["Expenses"]
        self.__loged_user_idx = -1
        self.__tenants_list = self.__dic["TenantList"]
        # TODO
        print("TenantList:")
        print(self.__tenants_list)
        self.__rent_records = self.__dic["RentRecord"]
        # self.__tenantScreen = TenantInputScreen(self.__tenants_list)

    def loginMainMenu(self):
        self.print_menus(1)
        self.logon_menu()
        self.__tenantList = \
            TenantList(self.__tenants_list[self.__loged_user_idx])
        self.__tenantScreen = TenantInputScreen(self.__tenantList)

        scanner = ''
        while (scanner != 'q'):
            self.print_menus(2)
            scanner = input('Enter Value: ')

            if scanner.lower() == 'i':
                self.print_menus(3)
                scanner_2 = input('Enter Value: ')
                self.inputScreen(scanner_2)
            elif scanner.lower() == 'd':
                self.print_menus(4)
                scanner_2 = input('Enter Value:')
                self.output_screen(scanner_2)
        print('Thank you For using the Bookings System See you soon!')

    def inputScreen(self, scanner_2):
        if scanner_2 == 't':
            self.__tenants_list[self.__loged_user_idx] = \
                self.__tenantScreen.inputTenant()
            # TODO: convert into format here for JSON storage

            # tenant = Tenant()
            # ten_list = TenantList(self.__tenants_list[self.__loged_user_idx],
            #                       self.__rent_records[self.__loged_user_idx])
            # ten_list.inputTenant(tenant.getTenant(), tenant.getApt())
            # TODO idea: return or save ten_list in UI class for output
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
        else:
            print('\nGoing Back to Main Menu...')
            time.sleep(0.5)
        # TODO remove next line when TenanList converted to what is used outside
        if scanner_2 != 't':
            self.store_to_file()

    # Output Screen thing
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
        user_list = User_List(self.__user_list, self.__password,
                              self.__tenants_list, self.__rent_records,
                              self.__expenses_List)
        print('1) Enter a User')
        print('2) Create New User')
        login = input('Enter Value: ')

        while user_list.flag is False:
            if login == '1':
                user = User.user_wb()
                user_list.return_user(user.get_user())
                self.__loged_user_idx = user_list.get_logged_idx()
            elif login == '2':
                user = User.user_new()
                user_list.add_user(user.get_user())
                print('New User Logged In...\n')
                self.store_to_file()
                self.__loged_user_idx = user_list.get_logged_idx()
            else:
                print('Invalid Entry, Try Again...\n')
                login = input('Enter Value: ')

    def print_menus(self, num):
        if num == 1:
            print('Welcome to the Apartment Management System v0.1')
            print('Please select one of the following options:\n\n')
        elif num == 2:
            print('\nEnter \'i\' to Input data,')
            print('      \'d\' to Display data, or')
            print('      \'q\' to Quit the program.')
        elif num == 3:
            print('\nPlease Select One of the Following:')
            print('Enter \'t\' to add or Replace a Tenant,')
            print('      \'r\' to record a rent payment,')
            print('      \'e\' to record an expense payment, or')
            print('      press [Enter] to return to the main menu.')
        # For output_screen
        elif num == 4:
            print('\nPlease Select One of the Following:')
            print('Enter \'t\' to display Tenant List,')
            print('      \'r\' to display Rent Records,')
            print('      \'e\' to display Expense Records,')
            print('      \'a\' to display Annual Summary, or')
            print('      press [Enter] to return to the main menu.')
        else:
            print(f"Menu number {num} not supported.")

    def store_to_file(self):
        js = json.dumps(self.__dic)
        f = open("login.json", "w")
        f.write(js)
        f.close()


def main():
    ui = UserInterface()
    ui.loginMainMenu()


if __name__ == "__main__":
    main()
