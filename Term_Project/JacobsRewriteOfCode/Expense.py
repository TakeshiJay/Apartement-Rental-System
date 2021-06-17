from ExpenseInputScreen import ExpenseInputScreen


class Expense:
    def __init__(self):
        eis = ExpenseInputScreen.inputExpense()
        self.__month, self.__day, self.__category, self.__payee,
        self.__amount = eis.inputExpense()

    # FIXME  we use a single get to return everything
    def get_month(self):
        return(self.__month)

    def get_day(self):
        return(self.__day)

    def get_category(self):
        return(self.__category)

    def get_payee(self):
        return(self.__payee)

    def get_amount(self):
        return(self.__amount)
