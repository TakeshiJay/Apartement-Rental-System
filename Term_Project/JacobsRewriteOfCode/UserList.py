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
