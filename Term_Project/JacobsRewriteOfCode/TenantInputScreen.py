# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# @author Sterling Engle           #
# @author Matthew Chung            #
# @author Larry Delgado            #
# @author Jacob Sunia              #
#                                  #
# Due TBD at 23:59 PDT             #
# Finished: TBD at TBD             #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""


import re  # to use reqular expressions
from Tenant import Tenant


class TenantInputScreen:  # Tenant input screen
    def __init__(self, existingTenantList):
        self.__existingTenants = existingTenantList
        self.__aptNum = -1
        self.__tenantName = None

    def getTenant(self):
        return(self.__tenantName, self.__aptNum)

    def inputTenant(self):
        aptStr = input("Apartment # (-# to remove): ")
        if re.match("[-+]?\d+$", aptStr) is None:
            return self.__existingTenants
        self.__aptNum = int(aptStr)
        if self.__aptNum == 0:
            return self.__existingTenants
        existing = self.__existingTenants.findTenant(abs(self.__aptNum))

        if existing is not None:
            if self.__aptNum < 0:
                tenant = existing.getTenant()
                if tenant == "":
                    tenant = "is vacant."
                else:
                    tenant = "assigned to " + existing.getTenant()
                delete = input(f"Apartment {self.__aptNum} {tenant}. Remove"
                               " from building (y/n)? ").lower()
                if delete != 'y':
                    return self.__existingTenants
                else:
                    self.__tenantName = ""
            elif existing.getTenant() != "":
                replace = input(f"Apartment {self.__aptNum} already assigned "
                                f"to {existing.getTenant()}."
                                " Replace or vacate (y/n)? ").lower()
                if replace != 'y':
                    return self.__existingTenants
                else:
                    self.__tenantName = input("New tenant name "
                                              "or [Enter] to vacate: ")
            else:
                self.__tenantName = input("Tenant name: ")
        elif self.__aptNum > 0:
            self.__tenantName = input("Tenant name: ")

        newTenant = Tenant(self.__aptNum, self.__tenantName)
        tenant = self.__existingTenants.insertTenant(newTenant)
        if self.__aptNum > 0:
            if self.__tenantName != "":
                print(f"Apartment {tenant.getApt()} assigned "
                      f"to {tenant.getTenant()}.")
            elif existing is None:
                print(f"Apartment {tenant.getApt()} already vacant.")
            else:
                print(f"Apartment {tenant.getApt()} vacated.")
        elif existing is not None:
            print(f"Apartment {-self.__aptNum} removed from building.")
        else:
            print(f"Apartment {-self.__aptNum} not found -"
                  " not removed from building.")
        return self.__existingTenants
