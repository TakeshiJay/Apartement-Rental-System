class RentInputScreen:  # rental input screen
    def __init__(self, Name, month, amount):
        self.__Name = Name
        self.__month = month
        self.__amount = amount

    def getRent(self):
        return(self.__Name, self.__month, self.__amount)

    @classmethod
    def inputRentPayment(cls):
        return(cls(
            input('Enter Tenant Name: '),
            int(input('Enter Month No.: ')),
            float(input('Enter Rent Payment: '))
            )
        )
