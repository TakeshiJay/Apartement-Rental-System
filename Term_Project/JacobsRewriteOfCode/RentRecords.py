class RentRecords:
    def __init__(self, __rentRecord):
        self.__rentRecord = __rentRecord

    def insertRent(self, month, amount):
        self.__rentRecord[month-1] = amount

    #Get Rent Total
    def return_total_rent(self):
        rTotal = 0
        for key in __RentRecord:
            rTotal += __rentRecord[key]
        return rTotal
    
    #Print Rent Record
    def display(self):
        print("==== Rent Summary =====")
        print(self)
        #Tabulate
        '''
        headers = self.__Rent_List.keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
        '''
        #Print Rent Total Last
        print("\nRent Total: " + str(return_total_rent()))
        
