# -*- coding: utf-8 -*-
"""
########## Term Project ############
#                                  #
# owner: @author Sterling Engle    #
#                                  #
# Due Jun 24, 2021 at 11:59 PM PDT #
# Finished: Jun 20, 2021           #
#----------------------------------#
# CSULB CECS 343 Intro to S/W Engr #
# Professor Phuong Nguyen          #
####################################
"""


import re  # to use reqular expressions
from Tenant import Tenant


class TenantInputScreen:  # Tenant input screen

    # @param
    def __init__(self, tenantList):
        self.__tenants = tenantList
        self.__aptNum = -1  # apartment number
        self.__tenantName = None  # tenant name

    # get method returns tenant name and apartment number
    def getTenant(self):
        return(self.__tenantName, self.__aptNum)

    def inputTenant(self):
        while True:
            aptStr = input("Apartment # (-# to remove): ")
            if re.match("[-+]?\d+$", aptStr) is None:
                print(f'Invalid input "{aptStr}". Apartment # must be a '
                      'positive or negative number.')
                continue
            self.__aptNum = int(aptStr)
            if self.__aptNum == 0:
                print(f'Invalid input "{aptStr}. Apartment # must be a '
                      'non-zero positive or negative number.')
                return self.__tenants
            break

        existing = self.__tenants.findTenant(abs(self.__aptNum))
        if existing is not None:
            if self.__aptNum < 0:
                tenant = existing.getTenant()
                if tenant == "":
                    tenant = "is vacant."
                else:
                    tenant = "assigned to " + existing.getTenant()
                delete = input(f"Apartment {abs(self.__aptNum)} {tenant}."
                               " Remove from building (y/n)? ").lower()
                if delete != 'y':
                    return self.__tenants
                else:
                    self.__tenantName = ""
            elif existing.getTenant() != "":
                replace = input(f"Apartment {self.__aptNum} already assigned "
                                f"to {existing.getTenant()}."
                                " Replace or vacate (y/n)? ").lower()
                if replace != 'y':
                    return self.__tenants
                else:
                    self.__tenantName = input("New tenant name "
                                              "or [Enter] to vacate: ")
            else:
                self.__tenantName = input("Tenant name: ")
        elif self.__aptNum > 0:
            self.__tenantName = input("Tenant name: ")

        newTenant = Tenant(self.__aptNum, self.__tenantName)
        tenant = self.__tenants.insertTenant(newTenant)
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
        return self.__tenants
