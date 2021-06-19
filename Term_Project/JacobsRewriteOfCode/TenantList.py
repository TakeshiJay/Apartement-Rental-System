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


# The TenantList class maintains a list of Tenant objects in private memory
# and provides public methods for list manipulation and output.
class TenantList:

    # __init__(self) function is the overloaded class constructor
    def __init__(self, tenantList):
        self.__tenants = tenantList

    # returns index position of apartment number and/or tenant name in list,
    # else None.
    def __getTenantPos(self, aptNum=None, tenantName=None):
        for pos in range(self.countTenants()):
            aNum, tName = self.__tenants[pos].getAptTenant()
            if aptNum is not None and aptNum == aNum:
                if tenantName is None or tenantName == tName:
                    return pos
            elif tenantName is not None and tName == tenantName:
                if aptNum is None or aptNum == aNum:
                    return pos
        return None

    # insertTenant adds newTenant name to provided apartment number
    # if the apartment number is negative, it deletes abs(apartment number) if
    # it exists, else None is returned.
    def insertTenant(self, newTenant):
        aNum, tName = newTenant.getAptTenant()
        if aNum == 0:  # Apartment 0 invalid
            return None
        pos = self.__getTenantPos(abs(aNum))  # existing tenant in apt?
        if pos is not None:
            if aNum < 0:
                self.__tenants.pop(pos)  # delete apartment
            else:
                self.__tenants[pos] = newTenant  # replace existing tenant
        else:
            if aNum < 0:
                return None  # tried to delete non-existent apartment number
            else:
                self.__tenants.append(newTenant)  # add new tenant
        self.__tenants.sort(key=lambda t: t.getApt())  # sort in place
        return newTenant

    # countTenants returns the number of Tenant objects in the tenants list
    def countTenants(self):
        return len(self.__tenants)

    # countAptsTenants returns the number of apartments and tenants in list
    def countAptsTenants(self):
        occupied = filter(lambda t: t.aptOccupied(), self.__tenants)
        # https://stackoverflow.com/questions/19182188/how-to-find-the-length-of-a-filter-object-in-python
        return len(self.__tenants), sum(1 for _ in occupied)

    def getTenant(self, pos):
        if pos < self.countTenants() and pos > -1:
            return self.__tenants[pos]
        else:
            return None

    def findTenant(self, aptNum=None, tenantName=None):
        pos = self.__getTenantPos(aptNum=aptNum, tenantName=tenantName)
        if pos is not None:
            return self.__tenants[pos]
        else:
            return None

    def __str__(self):
        str = ""
        for i in range(self.countTenants()):
            str += self.getTenant(i).__str__() + "\n"
        return str

    def display(self):
        print("Apt # Tenant Name")
        print("----- -----------")
        print(self)
        return
