# -*- coding: utf-8 -*-

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

# The apartment class stores every instance of a Tenate into our class. It is simply an array
# of Tenate objects in the apartment building
class Apartment:
    
    # init function is the default constructor(A.K.A the place where all of our Tenate objects are
    # stored) This constructor runs in a time complexity of T(n) = Θ(1) based on initialization of 
    # our tenants list. 
    # @param tenants_list is the list of our objects
    # @param monthly_expenses is the list of expense objects 
    def __init__(self):
        self.tenant_list = []
        self.monthly_expenses = []
    
    # add tenant function will store our new tenant into our apartment bookings. It is simple a 
    # append function for our program to store new objects into our apartment. This function runs in
    # a time complexity of T(n) = Θ(1) based off of our append to the back of our array
    # @param tenant is the new tenate that will be stored into our apartment
    def add_tenant(self, tenant):
        if tenant not in self.tenant_list:
            self.tenant_list.append(tenant)
    
    # remove tenant function is used to remove a tenant from our apartment list. The time complexity
    # of our remove function runs in T(n) = O(n) based off our iteration through the tenant list 
    # @param name is the name of the tenant we are bound to remove
    def remove_tenant(self, name):
        for i in self.tenant_list:
            if i.Name == name:
                self.tenant_list.remove(i)
    
    # add expenses function adds newly created expenses to our list of expenses paid and reports the 
    # specific day, month, category, payee, and amount from the LandLord(John Nguyen). The time 
    # complexity of this function runs in T(n) = Θ(1) based on the simple append to our list of expenses
    # this list is not sorted and all based off of what is recorded at that moment in time.
    # @param expense is the expense object that will be defined depending on our users input.
    def add_expenses(self,expense):
        self.monthly_expenses.append(expense)

# tenant class will be used to help assist our apartment class which the objects
# will be appended to our apartment list
class Tenant:
    
    # init function is the overloaded constructor for our class
    # @param Name is the name of our tenant
    # @param Apart_No is an integer that will determine our apartment Number
    def __init__(self, Name, Apart_No):
        self.Name = Name
        self.Apart_No = Apart_No
        self.payment_list = [0]*11 # an list of 12 zero elements(12 representing the No. of months in a year)
        
    # record_payment function will be our transaction amount that will be
    # recorded in our bookings. All information stored will be directed by 
    # our user
    # @param index is the month that we will store our amount at
    # @param amount is the amount of money that will be stored at the given index
    def record_payment(self, index, amount):
        self.payment_list.insert(index, amount)
        
    # print_rental_income will be like a _toString_ function when we print out the monthly
    # payments for each person in the bookings. Its main priority is to print each persons 
    # apartment number and rental income as follows. This function runs in a time complexity
    # of T(n) = Θ(1) such that we are only printing out the payment list and apartment number
    def print_rental_income(self):
        #Prints as follows(Apartment Number-> print list and separate by n spaces)
        print(self.Apart_No, *self.payment_list, sep=" ")

# Expenses class will be our object that holds information on each expense. The whole purpose of this class
# is to keep all categories that belong under an expense into an instance. That will eventually be stored
# in our Apartments monthly expenses list of items 
class Expenses:
    
    # __init__ function is our overloaded constructor and serves the purpose of creating an object for the 
    # expenses class. The whole focus here is to keep all information linked for future use. The time 
    # complexity of this function runs in a time of T(n) = Θ(1) because we are only defining what an expense 
    # consists of 
    # @param month represents the month which the payment was made on
    # @param day represents the day which the payment was made on
    # @param category represents the category which the payment follows under
    # @param payee represents the person/company/firm/etc. which the payment was paid to
    # @param amount is the transaction amount that will be sent to our payee
    def __init__(self, month, day, category, payee, amount):
        self.month = month
        self.day = day
        self.category = category
        self.payee = payee
        self.amount = amount
          
# user class is a valid user that will be able to check out the apartment books program.
class user:
    
    # __init__ function is our overloaded constructor that creates a basic login system for any new users
    # @param user_name will be the user_name for our user object
    # @param password will be the password for our login system where user_name must match with password
    # @param apartment will be the apartment which our user will be assigned to but also taking into consideration
    # that there could be multiple apartments in arbitrary examples
    # @param role will control what functionalities the user is able to do in the program
    def __init__(self, user_name, password, apartment, role):
        self.user_name = user_name
        self.password = password
        self.apartment = apartment
        self.role = role

# valid_user class is basically a list of all users and identifying if a user is in our list of users
# if a user gives incorrect information validation will flag that user does not exist or will prompt to 
# create a new user
class valid_users:
    
    # __init__ function is our default constructor for our valid users class. The whole purpose is to store all 
    # valid user objects in a that are created. 
    def __init__(self):
        self.user_list = []
    
    # add_user class simply adds a new user to our user_list based on obeject reference point. If the user has
    # been added to the list then no action will be taken
    # @param user is the memory address of our user. 
    def add_user(self, user):
        if user not in self.user_list:
            self.user_list.append(user)
    
    # validation function is a simple ensurance that the user enters the correct password(CASE SENSITIVE). If the 
    # user enters the wrong password or invalid username the user will be either prompted to retry or create a new 
    # user.
    # @param user_name_in will be the user name checked at the login terminal 
    # @param password_in will be the password checked at the login terminal
    def validation(self, user_name_in, password_in):
        for i in self.user_list:
            if (i.user_name == user_name_in) and (i.password == pasword_in):
                return True
        return False
        
        
# tn = tenant("Jacob",343)
# ex = Expenses(1,2,"Insurance","All State",4840.0)
# month = 1
# tn.record_payment(month-1,1200)

# print("AptNo Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
# tn.print_rental_income()
# print(tn.Name)
# print(ex.month,"/",ex.day, ex.category, ex.payee, ex.amount)

# for i in tn.payment_list:
#     print(i)
