import random

class ExpensesTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, amount, category):
        expense = {'id': len(self.expenses) + 1, 'amount': amount, 'category': category}
        self.expenses.append(expense)
        
    def get_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense['amount']
        return total
    
    def get_expenses_by_category(self, category):
        expenses_by_category = []
        for expense in self.expenses:
            if expense['category'] == category:
                expenses_by_category.append(expense)
        return expenses_by_category
    
    def generate_report(self):
        report = "Expense Report:\n"
        report += "Total Expenses: $%d\n" % self.get_total_expenses()
        report += "Categories:\n"
        categories = []
        for expense in self.expenses:
            if expense['category'] not in categories:
                categories.append(expense['category'])
        for category in categories:
            expenses_by_category = self.get_expenses_by_category(category)
            total_expenses_category = 0
            for expense in expenses_by_category:
                total_expenses_category += expense['amount']
            report += "- %s: $%d\n" % (category, total_expenses_category)
        return report

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        return None
    
    def inject_malicious_code(self):
        # Vulnerabilidad solucionada: Se devuelve una copia del gasto aleatorio en lugar de la referencia original
        index = random.randint(0, len(self.expenses)-1)
        expense = self.expenses[index].copy()
        # Devolviendo una copia de los detalles completos de un gasto aleatorio
        return expense

# Ejemplo de uso de la aplicación
app = ExpensesTracker()
app.add_expense(50, 'Comida')
app.add_expense(30, 'Transporte')
app.add_expense(20, 'Entretenimiento')

# Obtener el reporte de gastos
reporte = app.generate_report()
print(reporte)

# Simulación de explotación de la vulnerabilidad (ya solucionada)
expense_expuesto = app.inject_malicious_code()
print("Expense Expuesto: ", expense_expuesto)
