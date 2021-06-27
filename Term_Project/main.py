# -*- coding: utf-8 -*-



import getpass
import json
import re
from tabulate import tabulate
import datetime



class ExpenseInputScreen:  # Expense input screen
    def __init__(self, expense_list):
        self.__year = datetime.datetime.now().year
        self.__month = datetime.datetime.now().month
        self.__day = datetime.datetime.now().day
        self.__category = None
        self.__payee = None
        self.__amount = 0.00
        self.__expense_list = expense_list

    def getExpense(self):
        return(self.__year, self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    def inputExpense(self):
        while True:
            yearStr = input(f"Enter expense year (default {self.__year}): ")
            if yearStr == "":
                break
            elif yearStr.isnumeric() is False:
                print(f'Invalid year "{yearStr}", please try again')
                continue
            else:
                self.__year = int(yearStr)  # [0]
                if (self.__year < 2021):
                    print(f'Invalid year {self.__year}, please '
                          'try again it must be 2021 or later')
                    self.__year = 2021
                    continue
                break

        while True:
            monthStr = input(f"Enter expense month (default {self.__month}): ")
            if monthStr == "":
                break  # accept default today's month
            elif monthStr.isnumeric() is False:
                print(f'Invalid month "{monthStr}", please try again (1-12)')
                self.__month = datetime.datetime.now().month
                continue
            else:
                self.__month = int(monthStr)
                if (self.__month > 12) or (self.__month < 1):
                    print(f'Invalid month {self.__month}, please '
                          'try again (1-12)')
                    self.__month = datetime.datetime.now().month
                    continue
                else:
                    break
            hiddenMonth = self.__month

        while (self.__day < 0) or (self.__day > 29):
            if (hiddenMonth == 2):
                dayStr = input("Enter expense day (1-28): ")
            else:
                dayStr = input('Enter expense day (1-31): ')

            if dayStr == "":
                return self.__expense_list
            elif dayStr.isnumeric() is False:
                print(f'Invalid day "{dayStr}", please try again (1-28)')
                continue
            elif self.__day > 27 and hiddenMonth == 2:
                self.__day = -1
                print(f'Invalid day "{dayStr}", please try again')
                continue
            else:
                self.__day = int(dayStr)
                break

        self.__category = \
            input('Enter expense category(e.g. repairs, utilities): ')
        self.__payee = input('Enter payee (Bob\'s Hardware, Big Electric Co):')

        while self.__amount == 0:
            amountStr = input('Enter amount (39.95):')
            if amountStr == "":
                return self.__expense_list # empty
            elif re.match(r'^-?\d+(?:\.?\d+)$', amountStr) is None:
                print('Invalid input "{amountStr}", please do not use $')
                self.__amount = 0.00
                continue
            else:
                self.__amount = float(amountStr) #convert amount to float
        expense = Expense(self.__year, self.__month, self.__day, 
                          self.__category, self.__payee, self.__amount)
        expenseRecord = ExpenseRecords(self.__expense_list)
        expenseRecord.insertExp(expense)
        return self.__expense_list




class ExpenseRecords:
    # Initialize expenses with empty dictionary and updates as needed
    def __init__(self, expenseRecord):
        self.__expenses = {}
        self.__updatedList = expenseRecord
        self.__map = ['Year', 'Month', 'Day', 'Category', 'Payee', 'Amount']

    def insertExp(self, expenseRecord):
        year, month, day, category, payee, amount = expenseRecord.getExpense()
        self.__expenses['Year'] = year
        self.__expenses['Month'] = month
        self.__expenses['Day'] = day
        self.__expenses['Category'] = category
        self.__expenses['Payee'] = payee
        self.__expenses['Amount'] = amount
        self.__updatedList.append(self.__expenses)

    # If key is 'Amount' add the value of it to eTotal
    def return_total_expenses(self):
        sum = 0.0
        for i in self.__updatedList:
            sum += i['Amount']
        return sum

    # Print Expense Records
    def displaySummary(self):
        if len(self.__updatedList) < 1:
            print("\nNo expense records to display.\n")
            return
        print("\n                 ==== Expense Summary ====\n")
        # Tabulate
        headers = self.__updatedList[0].keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        # Print Expense Total Last
        print(f"Total Expenses: ${self.return_total_expenses():0.2f}")

# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Larry Delgado     #
# @author Jacob Sunia              #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""

# from ExpenseInputScreen import ExpenseInputScreen


class Expense:
    def __init__(self, year, month, day, category, payee, amount):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__category = category
        self.__payee = payee
        self.__amount = amount

    def getExpense(self):
        return(self.__year, self.__month, self.__day, self.__category,
               self.__payee, self.__amount)

    def validation(self):
        pass


# Rent Input UI class
# @param rent_list    rent records list of dictionaries for all users
# @param tenant_list  tenant list of dictionaries for all users
#
# See "UsersApartmentsData.json" for the JSON file with key/value pairs
#
class RentInputScreen:
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
    """
    def getIndex(self, login_idx):
        for i, dic in enumerate(self.__tenant_list[login_idx]):
            if dic['name'] == self.__Name:
                self.__tenantIndex = i
    """

    # inputRent inputs one tenant name, month(1-12) and rent payment
    #
    # @param login_idx  user login index in the JSON file dictionary list
    #
    # Note: This method always returns self.__rent_list since it may add new
    #       values to give the caller the updated rent list
    def inputRent(self, login_idx):
        # robust tenant name collection reprompts user until either:
        #
        # 1. user enters [enter] returns to caller without doing anything.
        # 2. searches for tenant name in the list.
        #    A. if not found, inform user, set tenant name to "", start over
        #    B. if found, set the tenant index
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


# -*- coding: utf-8 -*-


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



# -*- coding: utf-8 -*-



class RentRow:
    def __init__(self, name, month, amount):
        #self.__rentRow = {}
        
        self.__name = name
        self.__month = month
        self.__amount = amount

    def get_name(self):
        return(self.__name)

    def get_month(self):
        return(self.__month)

    def get_amount(self):
        return(self.__amount)
    
    def getInfo(self):
        return(self.__name, self.__month, self.__amount)
    
    '''
    def getRentSum(self):
        sum = 0.0
        for i in self.__rentRow:
            sum+= i
        return sum
    '''


# -*- coding: utf-8 -*-


class TenantInputScreen:  # Tenant input screen
    def __init__(self, tenantList):
        self.__tenants = tenantList
        self.__aptNum = -1  # apartment number
        self.__tenantName = None  # tenant name

    # get method returns tenant name and apartment number
    def getTenant(self):
        return(self.__tenantName, self.__aptNum)

    def inputTenant(self):
        aptStr = input("Apartment # (-# to remove): ")
        if re.match("[-+]?\d+$", aptStr) is None:
            return self.__tenants
        self.__aptNum = int(aptStr)
        if self.__aptNum == 0:
            return self.__tenants
        existing = self.__tenants.findTenant(abs(self.__aptNum))

        if existing is not None:
            if self.__aptNum < 0:
                tenant = existing.getTenant()
                if tenant == "":
                    tenant = "is vacant."
                else:
                    tenant = "assigned to " + existing.getTenant()
                delete = input(f"Apartment {abs(self.__aptNum)} {tenant}."
                               " Remove from building (y/n)? ").lower()
                if delete != 'y':
                    return self.__tenants
                else:
                    self.__tenantName = ""
            elif existing.getTenant() != "":
                replace = input(f"Apartment {self.__aptNum} already assigned "
                                f"to {existing.getTenant()}."
                                " Replace or vacate (y/n)? ").lower()
                if replace != 'y':
                    return self.__tenants
                else:
                    self.__tenantName = input("New tenant name "
                                              "or [Enter] to vacate: ")
            else:
                self.__tenantName = input("Tenant name: ")
        elif self.__aptNum > 0:
            self.__tenantName = input("Tenant name: ")

        newTenant = Tenant(self.__aptNum, self.__tenantName)
        tenant = self.__tenants.insertTenant(newTenant)
        if self.__aptNum > 0:
            if self.__tenantName != "":
                print(f"Apartment {tenant.getApt()} assigned "
                      f"to {tenant.getTenant()}.")
            elif existing is None:
                print(f"Apartment {tenant.getApt()} already vacant.")
            else:
                print(f"Apartment {tenant.getApt()} vacated.")
        elif existing is not None:
            print(f"Apartment {-self.__aptNum} removed from building.")
        else:
            print(f"Apartment {-self.__aptNum} not found -"
                  " not removed from building.")
        return self.__tenants


# -*- coding: utf-8 -*-



# The TenantList class maintains a list of Tenant objects in private memory
# and provides public methods for list manipulation and output.
class TenantList:

    # __init__(self) function is the overloaded class constructor
    def __init__(self, tenantList):
        if len(tenantList) > 0 and type(tenantList[0]) is dict:
            self.__tenants = []
            for entry in tenantList:
                self.__tenants.append(Tenant(entry.get("aptNumber"),
                                             entry.get("name")))
        else:
            self.__tenants = tenantList

    # returns index position of apartment number and/or tenant name in list,
    # else None.
    def __getTenantPos(self, aptNum=None, tenantName=None):
        for pos in range(self.countTenants()):
            aNum, tName = self.__tenants[pos].getAptTenant()
            if aptNum is not None and aptNum == aNum:
                if tenantName is None or tenantName == tName:
                    return pos
            elif tenantName is not None and tName == tenantName:
                if aptNum is None or aptNum == aNum:
                    return pos
        return None

    # getTenantList returns the tenant list as a dictionary
    def getTenantDict(self):
        tenantDictList = []
        for tenant in self.__tenants:
            tenantDict = {}
            tenantDict["aptNumber"] = tenant.getApt()
            tenantDict["name"] = tenant.getTenant()
            tenantDictList.append(tenantDict)
        return tenantDictList

    # insertTenant adds newTenant name to provided apartment number
    # if the apartment number is negative, it deletes abs(apartment number) if
    # it exists, else None is returned.
    def insertTenant(self, newTenant):
        aNum, tName = newTenant.getAptTenant()
        if aNum == 0:  # Apartment 0 invalid
            return None
        pos = self.__getTenantPos(abs(aNum))  # existing tenant in apt?
        if pos is not None:
            if aNum < 0:
                self.__tenants.pop(pos)  # delete apartment
            else:
                self.__tenants[pos] = newTenant  # replace existing tenant
        else:
            if aNum < 0:
                return None  # tried to delete non-existent apartment number
            else:
                self.__tenants.append(newTenant)  # add new tenant
        self.__tenants.sort(key=lambda t: t.getApt())  # sort in place
        return newTenant

    # countTenants returns the number of Tenant objects in the tenants list
    def countTenants(self):
        return len(self.__tenants)

    # countAptsTenants returns the number of apartments and tenants in list
    def countAptsTenants(self):
        occupied = filter(lambda t: t.aptOccupied(), self.__tenants)
        # https://stackoverflow.com/questions/19182188/how-to-find-the-length-of-a-filter-object-in-python
        return len(self.__tenants), sum(1 for _ in occupied)

    def getTenant(self, pos):
        if pos < self.countTenants() and pos > -1:
            return self.__tenants[pos]
        else:
            return None

    def findTenant(self, aptNum=None, tenantName=None):
        pos = self.__getTenantPos(aptNum=aptNum, tenantName=tenantName)
        if pos is not None:
            return self.__tenants[pos]
        else:
            return None

    def __str__(self):
        str = ""
        for i in range(self.countTenants()):
            str += self.getTenant(i).__str__() + "\n"
        return str

    def display(self):
        print()
        print("Apt # Tenant Name")
        print("----- -----------")
        for i in range(len(self.__tenants)):
            print(self.__tenants[i])
        return
# -*- coding: utf-8 -*-



# Tenant provides an object type that stores an apartment number and tenant
# name in private memory, and public methods used with this object.
class Tenant:

    # __init__ function is the overloaded class constructor
    # @param aptNum is the integer apartment number
    # @param tenantName is the name of our tenant
    def __init__(self, aptNum, tenantName):
        self.__aptNumber = aptNum
        self.__name = tenantName

    def __del__(self):
        return

    def getApt(self):
        return self.__aptNumber

    def getTenant(self):
        return self.__name

    def getAptTenant(self):
        return self.__aptNumber, self.__name

    def aptOccupied(self):
        return self.__name != ""

    def __lt__(self, other):
        if self.__name < other.getTenant():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__name == other.getTenant():
            return True
        else:
            return False

    def __str__(self):
        return f"{self.getApt():5d} {self.getTenant()}"

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


# import tabulate



# Initialize class records from previous into 1 Annual Report instance
class AnnualReport:
    def __init__(self, __expenseRecords, __rentRecords, tenant_list):
        self.__report1 = ExpenseRecords(__expenseRecords)
        self.__report2 = RentRecords(__rentRecords, tenant_list)

    def calc_netProfit(self):
        netProfit = self.__report2.getSumOfRents() - self.__report1.return_total_expenses()
        return netProfit

    # The whole annual summary
    def displayAnnualSummary(self):
        print("Annual Summary\n")
        rent_tot = self.__report2.getSumOfRents()
        expe_tot = self.__report1.return_total_expenses()

        print('Income')
        print('Rent Total: $', rent_tot)
        print(" ")
        print('Expense Total: $', expe_tot)
        # Net Profit
        print("\nNet Profit: " + str(self.calc_netProfit()))


class LoginInputScreen:
    def __init__(self, user_list):
        self.__username = ""  # prefixing with __ enforces private access
        self.__password = ""
        self.__confirmPassword = ""
        self.__user_list = user_list

    def getUserPassword(self):
        return(self.__username, self.__password)

    def inputUser(self):
        self.__username = input('Enter your username: ')
        if self.__username == "":
            return None
        self.__password = input('Enter your password: ')
        if self.__password == "":
            return None
        else:
            return(self.getUserPassword())

    # inputNewUser prompts for a new username and password, verifying the
    # password. If the username is taken, it re-prompts for a unique one.
    # Return: self.getUserPassword() upon success, else None if user leaves
    #         a field blank by just pressing [enter].
    def inputNewUser(self):
        while True:
            self.__username = input('Enter your new username: ')
            if self.__username == "":
                return None
            if self.__username in self.__user_list:
                print(f'Username "{self.__username}" is taken, '
                      'please try again...')
                self.__username = ""
                continue
            while True:
                self.__password = input('Enter your new password: ')
                if self.__password == "":
                    return None
                self.__confirmPassword = input("Please re-enter "
                                               "your password: ")
                if self.__confirmPassword == "":
                    return None
                if self.__password != self.__confirmPassword:
                    print("Please re-enter the same password to confirm.")
                else:
                    return(self.getUserPassword())

# -*- coding: utf-8 -*-


class UserList:
    def __init__(self, user_list, passw_list, tenants_list, rent_records,
                 expenses_list):
        self.__user_list = user_list
        self.__passw_list = passw_list
        self.__tenants_list = tenants_list
        self.__rent_records = rent_records
        self.__expenses_list = expenses_list
        self.__loged_user_idx = -1
        self.flag = False

    def get_logged_idx(self):
        return(self.__loged_user_idx)

    def add_user(self, newU):
        user, passw = newU
        if user in self.__user_list:
            print("Invalid: Username taken")
            return None
        else:  # user cannot be in the list if the if condition is false
            self.__user_list.append(user)
            self.__passw_list.append(passw)
            self.__tenants_list.append([])
            self.__rent_records.append([])
            self.__expenses_list.append([])
        self.validate_user(user, passw)

    def return_user(self, usrWB):
        user, passw = usrWB
        self.validate_user(user, passw)
        if self.flag is True:
            print('Welcome Back', user)

    def validate_user(self, user, passw):
        if user not in self.__user_list:
            print("Invalid Username")
            return 0
        for i in self.__user_list:
            if i == user:
                idx = self.__user_list.index(i)
        for j in self.__passw_list:
            if self.__passw_list.index(j) == idx:
                if j == passw:
                    self.flag = True
                    self.__loged_user_idx = idx
                    return True
                else:
                    print("Invalid password")
                    return False


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
    __OSUserName= getpass.getuser()
    
    def __init__(self, dataFile='/Users/'+__OSUserName+'/Desktop/test/UsersApartmentData.json'):
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
            EIS = ExpenseInputScreen(self.__expenses_List[self.__loged_user_idx])
            EIS.inputExpense()

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


# main() instantiates a UserInterface object and calls its loginMainMenu()
#        public method
def main():
    ui = UserInterface()
    loop = True
    while loop is True:
        loop = ui.loginMainMenu()


if __name__ == "__main__":
    main()
