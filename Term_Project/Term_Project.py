########## Term Project ############
#                                  #
# @author Jacob Sunia              #
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
    # our tenates list. 
    # @param tenate_list is the list of our objects 
    def __init__(self):
        self.tenate_list = []
    
    # add tenate function will store our new tenate into our apartment bookings. It is simple a 
    # append function for our program to store new objects into our apartment. This function runs in
    # a time complexity of T(n) = Θ(1) based off of our append to the back of our array
    # @param tenate is the new tenate that will be stored into our apartment
    def add_tenate(self,tenate):
        if tenate not in tenate_list:
            self.tenate_list.append(tenate)
    
    # remove tenate function is used to remove a tenate from our apartment list. The time complexity
    # of our remove function runs in T(n) = O(n) based off our iteration through the tenates list 
    # @param name is the name of the tenate we are bound to remove
    def remove_tenate(self,name):
        for i in self.tenate_list:
            if i.Name == name:
                self.tenate_list.remove(i)

# Tenate class will be used to help assist our apartment class which the objects
# will be appended to our apartment list
class Tenate:
    # init function is the overloaded constructor for our class
    # @param Name is the name of our Tenate
    # @param Apart_No is an integer that will determine our apartment Number
    def __init__(self, Name, Apart_No):
        self.Name = Name
        self.Apart_No = Apart_No
        self.payment_list = [0]*11 # an empty list of 12 elements(12 being the No. of months in a year)
        
    # record_payment function will be our transaction amount that will be
    # recorded in our bookings. All information stored will be directed by 
    # our user
    # @param index is the month that we will store our amount at
    # @param amount is the amount of money that will be stored at the given index
    def record_payment(self, index, amount):
        self.payment_list.insert(index, amount)
        
tn = Tenate("Jacob",343)
print(tn.Name, tn.Apart_No)
month = 1
tn.record_payment(month-1,1200)

for i in tn.payment_list:
    print(i)
