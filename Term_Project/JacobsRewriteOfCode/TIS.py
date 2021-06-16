class TIS: #Tenant input screen
    def __init__(self, Name, AptNo):
        self.__Name = Name
        self.__AptNo = AptNo

    def get_input(self):
        return(self.__Name, self.__AptNo)

    @classmethod
    def user_inp(cls):
        return cls(
            input("Tenant Name:"),
            int(input("Tenant Apartment_No: "))
        )
        
