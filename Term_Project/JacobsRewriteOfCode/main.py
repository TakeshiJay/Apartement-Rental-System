# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Jacob Sunia       #
#        @author Sterling Engle    #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: June 19, 2021          #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################

This file contains the main() entry for the Apartment Management System program
"""


from UserInterface import UserInterface


# main() instantiates a UserInterface object and calls its loginMainMenu()
#        public method
def main():
    ui = UserInterface()
    loop = True
    while loop is True:
        loop = ui.loginMainMenu()


if __name__ == "__main__":
    main()
