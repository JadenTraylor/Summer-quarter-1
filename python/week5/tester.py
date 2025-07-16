import budget

myBudget = budget.BudgetManager(2500)
print("Total funds", myBudget.funds)

myBudget.AddBudget("Books", 100)
myBudget.AddBudget("Rent", 800)
myBudget.AddBudget("Car Note", 200)

myBudget.Spend("Books", 50)
myBudget.Spend("Rent", 800)
myBudget.Spend("Car Note", 200) 
        
myBudget.PrintBudget()