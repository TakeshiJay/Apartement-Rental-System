class EIS: #Expense input screen
    def __init__(self, month, day, category, payee, amount):
        self.__month = month
        self.__day = day
        self.__category = category
        self.__payee = payee
        self.__amount = amount
    
    def get_expense(self):
        return(self.__month, self.__day, self.__category,
              self.__payee, self.__amount)
    
    @classmethod
    def user_inp(cls):
        return cls(
            int(input("Month No.:")),
            int(input("Day No.:")),
            input("Category:"),         
            input("Payee:"),
            float(input("Amount.:"))
      )

