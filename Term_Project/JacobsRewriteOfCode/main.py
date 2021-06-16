from Tenant import Tenant
from Tenant_List import Tenant_List
from USER import User
from Expense import Expense
from Expense_List import Expense_List
from Rent_Row import Rent_Row
from Rent_List import Rent_List

import json

class UI: #user interface
    def __init__(self):
        f = open('login.json',)
        self.__dic = json.load(f)
        self.flag = False
        self.__expenses_List = self.__dic["Expenses"]
        self.__loged_user_idx = -1
        self.__tenants_list = self.__dic["TenantList"]
        self.__rent_records = self.__dic["RentRecord"]
    
    def nu_user(self):
        newU = User.user_new()
        user, passw = newU.get_user()
        if user in self.__dic["Username"]:
            print("Invalid: Username taken")
        if user not in self.__dic["Username"]:
            self.__dic["Username"].append(user)
            self.__dic["Password"].append(passw)
            self.__tenants_list.append([])
            self.__rent_records.append([])
            self.__expenses_List.append([])
        self.store_to_file()
        self.validate_user(user, passw)

    def return_user(self):
        usrWB = User.user_wb()
        user, passw = usrWB.get_user()
        self.validate_user(user, passw)
        if self.flag == True:
            print('Welcome Back',user)

    def get_indx(self):
        return(self.__loged_user_idx)

    def validate_user(self, user, passw):
        if user not in self.__dic["Username"]:
            print("Invalid Username")
            return 0 
        for i in self.__dic["Username"]:
            if i == user:
                idx = self.__dic["Username"].index(i)
        for j in self.__dic["Password"]:
            if self.__dic["Password"].index(j) == idx:
                if j == passw:
                    self.flag = True
                    self.__loged_user_idx = idx
                    print("User/Password successful")
                    return 0 
                else:
                    print("Invalid Password")
                    return 0
    
    def store_to_file(self):
        js = json.dumps(self.__dic)
        f = open("login.json","w")
        f.write(js)
        f.close()

    def logon_menu(self):
        print('1) Enter a User')
        print('2) Create New User')
        login = input('Enter Value:')

        while self.flag == False:
            if login == '1':
                self.return_user()
            elif login == '2':
                self.nu_user()
                print('New User Logged In...\n')
            else:
                print('Invalid Entry, Try Again...\n')
                login = input('Enter Value:')

    def main(self):
        print('Welcome to the Apartment Complex System')
        print('Please Enter one of the following...\n\n')
        self.logon_menu()
  
        scanner = ''
        while(scanner != 'q' and self.flag == True):
            print('\nEnter \'i\' to input data,')
            print('Enter \'d\' to display data,')
            print('Enter \'q\' to quit the program')
            scanner = input('Enter Value:')
            
            if scanner.lower() == 'i':
                print('\nPlease Select One of the Following')
                print('Enter \'t\' to add a New Tenant,')
                print('Enter \'r\' to record a rent payment,')
                print('Enter \'e\' to record an expense payment')
                scanner_2 = input('Enter Value:')
                if scanner_2 == 't':
                    tenant = Tenant()
                    ten_list = Tenant_List(self.__tenants_list[self.__loged_user_idx], self.__rent_records[self.__loged_user_idx])
                    ten_list.add_nu_tenant(tenant.get_Tenant(),tenant.get_Apt())
                    
                    self.store_to_file()
            else:
                scanner = 'q'

ui = UI()
ui.main()
