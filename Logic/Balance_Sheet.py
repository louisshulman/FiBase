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


def Assets(c, accr, inv, pree, lndc, bldc, eqmtc):
    cash = c
    accounts_receivable = accr
    inventory = inv
    Prepaid_expenses = pree
    landcst = lndc
    buildingscst = bldc
    equipmentcst = eqmtc
    Fixed_assets = landcst + buildingscst + equipmentcst
    
    print("Cash $" + str(cash))
    print("Accounts Receivable $" + str(accounts_receivable))
    print("Inventory $" + str(inventory))
    print("Prepaid Expenses $" + str(Prepaid_expenses))
    print("Fixed Assets $" + str(Fixed_assets))
def Liabilities(ap, al, cp, tp, sd, ld):
    accounts_payable = ap
    accrued_liabilities = al
    customer_prepayment = cp
    tax_payable = tp
    shortterm_debt = sd
    longterm_debt = ld

    print("Accounts Payable $" + str(accounts_payable))
    print("Accrued Liabilities $" + str(accrued_liabilities))
    print("Customer Prepayment $" + str(customer_prepayment))
    print("Short-Term Debt $" + str(shortterm_debt))
    print("Long-Term Debt $" + str(longterm_debt))
def Equity():
