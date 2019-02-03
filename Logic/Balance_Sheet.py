#Assets
cash = input()
accounts_receivable = input()
inventory = input()
Prepaid_expenses = input()
landcst = input()
buildingscst = input()
equipmentcst = input()
Fixed_assets = landcst + buildingscst + equipmentcst

#Liabilities
accounts_payable = input()
accrued_liabilities = input()
customer_prepayment = input()
tax_payable = input()
shortterm_debt = input()
longterm_debt = input()

#Equity
Stock = input()

Assets = []
Liabilities = []
Equity = []
def Assetsplug(plug):
    Assets.append(plug)

def Liabilitiesplug(plug):
    Liabilities.append(plug)

def Equityplug(plug):
    Equity.append(plug)

def BalanceSheet():
    Sass = sum(Assets)
    Sliab = sum(Liabilities)
    Sequity = sum(Equity)
    if Sass == (Sliab + Sequity):
        print("Assets = $" + str(Sass))
        print("Liabilities = $" + str(Sliab))
        print("Equity = $" + str(Sequity))
        print("Books are balanced")
