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
