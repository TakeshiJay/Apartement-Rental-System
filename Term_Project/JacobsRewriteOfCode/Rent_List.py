class Rent_List:
    def __init__(self, __Rent_List):
        self.__Rent_List = __Rent_List
    
    def add_nu_renPayment(self, month, amount):
        self.__Rent_List[month-1] = amount