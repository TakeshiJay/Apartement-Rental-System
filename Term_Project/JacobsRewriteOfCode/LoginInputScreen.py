# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Sterling Engle           #
# @author Jacob Sunia              #
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
        # TODO Jacob: please check here if the username is used already
        while True:
            self.__password = input('Enter your new password: ')
            if self.__password == "":
                return None
            self.__confirmPassword = input('Please re-enter your password: ')
            if self.__password == self.__confirmPassword:
                if self.__confirmPassword == "":
                    return None
                else:
                    return(self.getUserPassword())
