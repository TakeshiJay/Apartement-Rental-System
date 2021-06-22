  
# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Jacob Sunia       #
#        @author Sterling Engle    #
#        @author Larry Delgado     #
#        @author Matthew Chung     #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""
# JavaScript Object Notation, is an open standard file format and data
# interchange format that uses human-readable text to store and transmit data
# objects consisting of attribute–value pairs and arrays
# (or other serializable values)
import json  # json used to read and write from persistent storage data file
from LoginInputScreen import LoginInputScreen
from TenantList import TenantList
from TenantInputScreen import TenantInputScreen
from Expense import Expense
from ExpenseRecords import ExpenseRecords
from RentInputScreen import RentInputScreen
from RentRecords import RentRecords
from UserList import UserList
from AnnualReport import AnnualReport


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
    def __init__(self, dataFile='UsersApartmentData.json'):
        self.__dataFile = dataFile
        f = open(self.__dataFile, "r")
        self.__dic = json.load(f)
        f.close()
        self.__UserList = self.__dic["Username"]
        self.__password = self.__dic["Password"]
        self.__expenses_List = self.__dic["Expenses"]
        self.__loged_user_idx = -1
        self.__tenants_list = self.__dic["TenantList"]
        self.__rent_records = self.__dic["RentRecords"]
        self.__tenantList = None  # logged-in user TenantList
        self.__expenseRecords = None  # logged-in user ExpenseRecords
        self.__rentRecords = None  # logged-in user RentRecords

    def loginMainMenu(self):
        self.print_menus(1)
        logonStatus = 0  # 0 means not logged in, 1 = logged in, 2 = quit
        while logonStatus == 0:
            logonStatus = self.logon_menu()
            if logonStatus == 2:
                return False  # quit

        # Save logged-in user TenantList, ExpenseRecords and RentRecords
        # in self.__tenantList, self.__expenseRecords, and self.__rentRecords
        self.__tenantList = \
            TenantList(self.__tenants_list[self.__loged_user_idx])
        self.__tenantScreen = TenantInputScreen(self.__tenantList)
        # TODO

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
                print("Thank you for using the Apartment Rental System "
                      "by Team 6.")
                print("See you again soon!\n")
                return True
            else:
                print(f'"{scanner}" is an invalid option please try again.')
        return True

    def inputScreen(self, scanner_2):
        if scanner_2 == 't':
            self.__tenantList = self.__tenantScreen.inputTenant()
            self.__tenants_list[self.__loged_user_idx] = \
                self.__tenantList.getTenantDict()
            self.__rent_records[self.__loged_user_idx].append([0]*12)
        elif scanner_2 == 'r':
            RIS = RentInputScreen(self.__rent_records, self.__tenants_list)
            self.__rent_records = RIS.inputRent(self.__loged_user_idx)
        elif scanner_2 == 'e':
            expense = Expense()
            expense_List = \
                ExpenseRecords(self.__expenses_List[self.__loged_user_idx])
            expense_List.insertExp(expense.get_month(),
                                   expense.get_day(),
                                   expense.get_category(),
                                   expense.get_payee(),
                                   expense.get_amount())
            expense_List.displaySummary(self.__loged_user_idx)
            # we should move this line to output_screen

        self.store_to_file()

    # Output Screen
    def output_screen(self, scanner_2):
        if scanner_2 == 't':
            tenantList = TenantList(self.__tenants_list[self.__loged_user_idx])
            tenantList.display()
        elif scanner_2 == 'r':
            rentRecords = RentRecords(self.__rent_records, self.__tenants_list)
            rentRecords.display(self.__loged_user_idx)
        elif scanner_2 == 'e':
            expenseRecords = ExpenseRecords(self.__expenses_List[self.__loged_user_idx])
            expenseRecords.displaySummary()
        elif scanner_2 == 'a':
            annualReport = AnnualReport(self.__expenses_List[self.__loged_user_idx], self.__rent_records, self.__tenants_list[self.__loged_user_idx])
            annualReport.calc_netProfit()
            annualReport.displayAnnualSummary()

    def logon_menu(self):
        user = LoginInputScreen(self.__UserList)
        userList = UserList(self.__UserList, self.__password,
                            self.__tenants_list, self.__rent_records,
                            self.__expenses_List)

        while userList.flag is False:
            login = input("Enter 1 to login, 2 to create new user, "
                          "or 'q' to Quit: ")
            if login == '1':  # user login
                lis = LoginInputScreen(self.__UserList)
                user = lis.inputUser()
                if user is not None:
                    userList.return_user(user)
                    self.__loged_user_idx = userList.get_logged_idx()
            elif login == '2':  # create new user/password and login
                lis = LoginInputScreen(self.__UserList)
                user = lis.inputNewUser()
                if user is not None:
                    if userList.add_user(user) is None:
                        print(f'There is already a username "{user[0]}".')
                        return 0  # not logged in
                    else:
                        print(f'New user "{user[0]}" logged in...\n')
                        self.store_to_file()
                        self.__loged_user_idx = userList.get_logged_idx()
                        return 1  # logged in
            elif login.lower() == 'q':  # quit program
                return 2  # quit program
            else:
                print(f'"{login}" is an invalid entry, please try again.')
        return 1  # logged-in

    def print_menus(self, num):
        if num == 1:
            print("Welcome to the Apartment Rental System - "
                  "Multiuser Edition v0.4")
            print("Please select one of the following login options:")
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
        f = open(self.__dataFile, "w")
        f.write(js)
        f.close()
