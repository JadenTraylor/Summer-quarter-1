
funds = 2500

budgets = {}

expenses = {}

def AddBudget(name, amount):
    global funds 
    if name in budgets:
        raise ValueError("Budget for item alreaady exists")
    if amount > funds:
        raise ValueError("No can do, to much prize picks")
    budgets[name] = amount 
    funds -= amount 
    expenses[name] = 0 
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Not here buddy")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name] 
    return budgeted - spent

def PrintBudget():
    for  name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        reamainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
              f'{reamainingBudget}')
    

print("Total funds", funds)

AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car Note", 200)

Spend("Books", 50)
Spend("Rent", 800)
Spend("Car Note", 200)

PrintBudget()





