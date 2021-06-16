class RIS: #rental input screen
    def __init__(self, Name, month, amount):
        self.__Name = Name
        self.__month = month
        self.__amount = amount
    
    def get_rent(self):
        return(self.__Name, self.__month, self.__amount)

    @classmethod
    def user_inp(cls):
        return(cls(
            input('Insert Tenant Name'),
            int(input('Enter Month No.:')),
            float(input('Enter Payment Amount:'))
            )
        )