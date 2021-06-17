import tabulate
import ExpenseRecords
import RentRecords

#Class to be written by Larry

#Initialize class records from previous into 1 Annual Report instance
class AnnualReport:
    def __init__(self, __expenseRecords, __rentRecords):
        self.__report1 = ExpenseRecords(__expenseRecords)
        self.__report2 = RentRecords(__rentRecords)
        
    def calc_netProfit(self):
        netProft = RentRecords.return_total_rents() - ExpenseRecords.return_total_expenses()
        return netProfit
    #The whole annual summary
    def displayAnnualSummary(self):
        print("Annual Summary\n")
        self.__report2.display()
        print(" ")
        self.__report1.displaySummary()
        #Net Profit
        print("\nNet Profit: " +str(calc_netProfit()))
