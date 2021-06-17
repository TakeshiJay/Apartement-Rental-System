
from Tenant import Tenant
from TenantList import TenantList
from USER import User
from Expense import Expense
from ExpenseRecords import ExpenseRecords
from RentRow import RentRow
from RentRecords import RentRecords
from User_List Import User_List


import json # importing json to write and read from our file
import time # importing time to delay some processes that we need to slow down


# UI is our user interface class where it mostly consists of the login and menu process
# @param __dic is the current dictionary that is loaded onto our program with all
#              information regarding both the LandLord(s) and their tenants
class UserInterface:  #user interface

    # __init__ function is a default constructor that builds our User Interface. The
    # constructors main purpose is to provide ourselves with a space to print and prompt
    # our user(**LandLord**)
    # @param flag is our basic boolean operator letting us know if a user is logged in or not
    # @param __expenses_List is our extended list of dictionary expense items
    # @param __loged_user_idx is the current index of our logged in user. It's default
    # initially is set to -1 because there are no current logged in users
    # @param __tenants_list is the list of tenants that are currently living in one of our logged in users Apartment
    # @param __rent_records is a list of records throughout a yearly cycle and records
    # all tenant payment transactions
    def __init__(self):
        f = open('login.json', )
        self.__dic = json.load(f)
        self.__user_list = self.__dic["Username"]
        self.__password = self.__dic["Password"]
        self.__expenses_List = self.__dic["Expenses"]
        self.__loged_user_idx = -1
        self.__tenants_list = self.__dic["TenantList"]
        self.__rent_records = self.__dic["RentRecord"]

    def main(self):
        self.print_menus(1)
        self.logon_menu()

        scanner = ''
        while (scanner != 'q'):
            self.print_menus(2)
            scanner = input('Enter Value:')

            if scanner.lower() == 'i':
                self.print_menus(3)
                scanner_2 = input('Enter Value:')
                self.input_screen(scanner_2)
            if scanner.lower() == 'd':
                self.print_menus(4)
                scanner_2 = input('Enter Value:')
                self.output_screen(scanner_2)
        print('Thank you For using the Bookings System See you soon!')

    def input_screen(self, scanner_2):
        if scanner_2 == 't':
            tenant = Tenant()
            ten_list = TenantList(self.__tenants_list[self.__loged_user_idx],
                                   self.__rent_records[self.__loged_user_idx])
            ten_list.add_nu_tenant(tenant.get_Tenant(), tenant.get_Apt())
        elif scanner_2 == 'r':
            rent_row = RentRow()
            rent_list = RentRecords(self.__rent_records, self.__loged_user_idx,
                                  self.__tenants_list[self.__loged_user_idx])
            rent_list.add_nu_renPayment(rent_row.get_month(),
                                        rent_row.get_amount(),
                                        rent_row.get_name())
        elif scanner_2 == 'e':
            expense = Expense()
            expense_List = ExpenseRecords(
                self.__expenses_List[self.__loged_user_idx])
            expense_List.add_nu_expense(expense.get_month(),                                      
                                        expense.get_day(),
                                        expense.get_category(),
                                        expense.get_payee(),
                                        expense.get_amount())
            expense_List.print_expenses()
        else:
            print('\nGoing Back to Main Menu...')
            time.sleep(0.5)
        self.store_to_file()

    def logon_menu(self):
        user_list = User_List(self.__user_list, self.__password,
                              self.__tenants_list, self.__rent_records,
                              self.__expenses_List)
        print('1) Enter a User')
        print('2) Create New User')
        login = input('Enter Value:')

        while user_list.flag == False:
            if login == '1':
                user = User.user_wb()
                user_list.return_user(user.get_user())
                self.__loged_user_idx = user_list.get_logged_idx()
            elif login == '2':
                user = User.user_new()
                user_list.nu_user(user.get_user())
                print('New User Logged In...\n')
                self.store_to_file()
                self.__loged_user_idx = user_list.get_logged_idx()
            else:
                print('Invalid Entry, Try Again...\n')
                login = input('Enter Value:')

    def print_menus(self, num):
        if num == 1:
            print('Welcome to the Apartment Complex System')
            print('Please Enter one of the following...\n\n')
        if num == 2:
            print('\nEnter \'i\' to input data,')
            print('Enter \'d\' to display data,')
            print('Enter \'q\' to quit the program')
        if num == 3:
            print('\nPlease Select One of the Following')
            print('Enter \'t\' to add a New Tenant,')
            print('Enter \'r\' to record a rent payment,')
            print('Enter \'e\' to record an expense payment')

    def store_to_file(self):
        js = json.dumps(self.__dic)
        f = open("login.json", "w")
        f.write(js)
        f.close()


def main():
    ui = UserInterface()
    ui.main()


if __name__ == "__main__":
    main()