class BudgetManager:
    def __init__(self, amount):

        self.funds = amount

        self.budgets = {}

        self.expenses = {}

    def AddBudget(self, name, amount):
        if name in self.budgets:
              raise ValueError("Budget for item alreaady exists")
        if amount > self.funds:
            raise ValueError("No can do, to much prize picks")
        self.budgets[name] = amount 
        self.funds -= amount 
        self.expenses[name] = 0 
        return self.funds

    def Spend(self, name, amount):
        if name not in self.expenses:
            raise ValueError("Not here buddy")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name] 
        return budgeted - spent

    def PrintBudget(self):
        print("Budget            Budgeted       Spent    Reamaining")
        print("----------------------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for  name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            reamainingBudget = budgeted - spent
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
                f'{reamainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining += reamainingBudget
            print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f} '
                    f'{totalRemaining:10.2f}')
            
