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


from Tenant import Tenant
from TenantList import TenantList

""" This code does not confirm to our class diagrams will be removed soon:
    
class TenantInputScreen:  # Tenant input screen
    def __init__(self, Name, AptNum):
        self.__tenantName = Name
        self.__AptNum = AptNum

    def getTenant(self):
        return(self.__tenantName, self.__AptNum)

    @classmethod
    def inputTenant(cls):
        return cls(
            input("Tenant Name:"),
            int(input("Tenant Apartment_No: "))
        )
"""


class TenantInputScreen:  # Tenant input screen
    def __init__(self, existingTenantList):
        self.__existingTenants = existingTenantList
        self.__aptNum = -1
        self.__tenantName = None

    def getTenant(self):
        return(self.__tenantName, self.__aptNum)

    def inputTenant(self): 
        print(self.__existingTenants)
        self.__aptNum = int(input("Apartment #: "))
        existing = self.__existingTenants.findTenant(self.__aptNum)
        if existing is not None:
            replace = input(f"Apartment {self.__aptNum} assigned to {existing}."
                            " Replace tenant? (y/n)").lower()
            if replace != 'y':
                return self.__existingTenants

        self.__tenantName = input("Tenant name: ")
        newTenant = Tenant(self.__aptNum, self.__tenantName)
        tenant = self.__existingTenants.insertTenant(newTenant)
        return self.__existingTenants

