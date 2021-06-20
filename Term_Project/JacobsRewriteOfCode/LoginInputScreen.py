# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Sterling Engle    #
#        @author Jacob Sunia       #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: June 19, 2021          #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""


class LoginInputScreen:
    def __init__(self):
        self.__username = ""  # prefixing with __ enforces private access
        self.__password = ""
        self.__confirmPassword = ""

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

    def inputNewUser(self):
        self.__username = input('Enter your new username: ')
        if self.__username == "":
            return None
        if self.__username in self.__user_list:
            print('Username is taken, please try again...\n')
            self.inputNewUser() # recursively loop if the username is taken
        while True:
            self.__password = input('Enter your new password: ')
            if self.__password == "":
                return None
            self.__confirmPassword = input('Please re-enter your password: ')
            if self.__confirmPassword == "":
                return None
            if self.__password != self.__confirmPassword:
                print("Please re-enter the same password to confirm.")
            else:
                return(self.getUserPassword())
