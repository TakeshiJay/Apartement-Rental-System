import tabulate


class ExpenseRecords:
    def __init__(self, expenseList):
        self.__expenses = {}
        self.__updatedList = expenseList

    def add_nu_expense(self, month, day, category, payee, amount):
        self.__expenses['Month'] = month
        self.__expenses['Day'] = day
        self.__expenses['Category'] = category
        self.__expenses['Payee'] = payee
        self.__expenses['Amount'] = amount
        self.__updatedList.append(self.__expenses)

    def print_expenses(self):
        headers = self.__updatedList[0].keys()
        rows = [x.values() for x in self.__updatedList]
        print(tabulate.tabulate(rows, headers, tablefmt='rst'))
