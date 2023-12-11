import enterIncome
import enterExpense
import checkBalance

def main():
    operation = input("What do you want to do (choose the number of your preferred option)?\n1) Enter expense\n2) Enter income\n3) Enter income and budget\n4) Check budget\nE) Exit\nValue: ")
    if operation == "1":
        enterExpense.enterExpense()
    elif operation == "2":
        enterIncome.enterIncome()
    elif operation == "3":
        enterIncome.enterIncome()
        enterIncome.enterOrUpdateBudget()
        print("test.")
    elif operation == "4":
        checkBalance.checkBalance()
    elif operation == "e" or "E":
        exit
    else:
        raise ValueError ("Not a valid option.")
main()