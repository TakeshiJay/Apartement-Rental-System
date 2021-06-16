from RIS import RIS

class Rent_Row:
    def __init__(self):
        ris = RIS.user_inp()
        self.__Name, self.__month, self.__amount = ris.get_rent()

    def get_name(self):
        return(self.__Name)
    
    def get_month(self):
        return(self.__month)
    
    def get_amount(self):
        return(self.__amount)

