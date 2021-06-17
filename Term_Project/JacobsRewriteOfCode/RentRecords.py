class RentRecords:
    def __init__(self, __Rent_List):
        self.__Rent_List = __Rent_List

    def insertRent(self, month, amount):
        self.__Rent_List[month-1] = amount
