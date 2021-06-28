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
    # __init__ constructor for username and password
    # @param user_list 
    def __init__(self, user_list):
        self.__username = ""  # prefixing with __ enforces private access
        self.__password = ""
        self.__confirmPassword = ""
        self.__user_list = user_list

    # getuserPassword return function for username and passsword
    # @return __username, __password
    def getUserPassword(self):
        return(self.__username, self.__password)

    # inputUser is a function that gets username and password
    # @return getUsserPassword if passsword is not valid 
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
