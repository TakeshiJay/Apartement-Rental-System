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

from Tenant import Tenant
from TenantList import TenantList
import json


def TenantTenantListUnitTest():
    print("*** Tenant class unit test cases: ***")
    dataFile = 'UsersApartmentData.json'
    f = open(dataFile, "r")
    __dic = json.load(f)
    f.close()
    __tenants_list = __dic["TenantList"]

    t42 = Tenant(42, "")  # empty apartment
    t1 = Tenant(100, "Sterling Engle")
    t1apt, t1name = t1.getAptTenant()
    print(f"t1: Apt # = {t1apt}: Name = {t1name}")
    print(t1)
    t2 = Tenant(101, "Jacob Sunia")
    print(t2)
    if t2 < t1:
        print(t2, "sorts by name before", t1)
    else:
        print(t2, "sorts by name after", t1)
    if t1 == t1:
        print(t1, "name equals", t1)
    else:
        print(t1, "name is not equal to", t1)
    if t1 == t2:
        print(t1, "name equals", t2)
    else:
        print(t1, "name is not equal to", t2)
    t3old = Tenant(102, "Matthew McConaughey")
    t3 = Tenant(102, "Matthew Chung")
    t4 = Tenant(103, "Larry Delgado")
    print("")

    print("*** TenantList class unit test cases: ***")
    tlist = TenantList(__tenants_list[0])
    print("empty TenantList object display:")
    tlist.display()
    aCnt, tCnt = tlist.countAptsTenants()
    print(f"reported {aCnt} apartment(s) and {tCnt} tenant(s)")
    print("now put Larry in Apt # 103")
    tlist.insertTenant(t4)
    print("call print(tlist) to test __str__()")
    print(tlist)
    aCnt, tCnt = tlist.countAptsTenants()
    print(f"reported {aCnt} apartment(s) and {tCnt} tenant(s)")
    tlist.insertTenant(t3old)
    tlist.display()
    tlist.insertTenant(t1)
    tlist.insertTenant(t2)
    tlist.display()
    print("replace the actor with Matthew Chung in Apt # 102:")
    tlist.insertTenant(t3)
    tlist.display()
    print("see who is in Apt # 102 now?")
    t102 = tlist.findTenant(aptNum=102)
    print(t102)
    print("see what Apt # Sterling Engle is in?")
    tSterling = tlist.findTenant(tenantName="Sterling Engle")
    print(tSterling)
    print("is Jacob Sunia in Apt # 102?")
    print(tlist.findTenant(102, "Jacob Sunia"))
    print("is Jacob Sunia in Apt # 101?")
    print(tlist.findTenant(101, "Jacob Sunia"))
    print("replace Jacob with himself in Apt # 101")
    tlist.insertTenant(t2)
    print("call print(tlist) again")
    print(tlist)
    print("add Apt # 42 with no tenant:")
    tlist.insertTenant(t42)
    tlist.display()
    aCnt, tCnt = tlist.countAptsTenants()
    print(f"reported {aCnt} apartment(s) and {tCnt} tenant(s)")
    print("remove apt # 42 by using -42 apt #:")
    tlist.insertTenant(Tenant(-42, ""))
    tlist.display()
    aCnt, tCnt = tlist.countAptsTenants()
    print(f"reported {aCnt} apartment(s) and {tCnt} tenant(s)")
    print("")
    return
