from RentInputScreen import RentInputScreen


class RentRow:
    def __init__(self):
        ris = RentInputScreen.inputRentPayment()
        self.__name, self.__month, self.__amount = ris.inputRentPayment()

    def get_name(self):
        return(self.__name)

    def get_month(self):
        return(self.__month)

    def get_amount(self):
        return(self.__amount)
