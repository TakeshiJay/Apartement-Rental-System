class ExpenseInputScreen: #Expense input screen
    def __init__(self, month, day, category, payee, amount):
        self.__month = month
        self.__day = day
        self.__category = category
        self.__payee = payee
        self.__amount = amount
    
    def getExpense(self):
        return(self.__month, self.__day, self.__category,
              self.__payee, self.__amount)
    
    @classmethod
    def inputExpense(cls):
        return cls(
            int(input("Month No.:")),
            int(input("Day No.:")),
            input("Category:"),         
            input("Payee:"),
            float(input("Amount.:"))
      )

