class Expense_List:
    def __init__(self, __Expense_List):
        self.__Expense_List = {}
        self.__updated_List = __Expense_List

    def add_nu_expense(self, month, day, category, payee, amount):
        self.__Expense_List['Month'] = month 
        self.__Expense_List['Day'] = day
        self.__Expense_List['Category'] = category
        self.__Expense_List['Payee'] = payee
        self.__Expense_List['Amount'] = amount
        self.__updated_List.append(self.__Expense_List) 