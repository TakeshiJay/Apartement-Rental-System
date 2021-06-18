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

# from TenantInputScreen import TenantInputScreen

"""
SJE: Tenant class may not prompt to input a new tenant.
That would violate the object hierarchy since Tenant is at the lowest level.
code here temp. for historical reasons will be removed before 0.2 release

class Tenant:
    def __init__(self):
        tis = TenantInputScreen.inputTenant()
        self.__Apt_No, self.__Name = tis.getTenant()
    def getApt(self):
        return self.__Apt_No

    def getTenant(self):
        return self.__Name
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
