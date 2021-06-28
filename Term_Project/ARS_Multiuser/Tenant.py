# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Sterling Engle    #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: Jun 19, 2021           #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""


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
        return self.__name is not None and self.__name != ""

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
