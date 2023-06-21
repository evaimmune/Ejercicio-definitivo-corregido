from flask import Flask, render_template, request, redirect, url_for
import random
import matplotlib.pyplot as plt

app = Flask(__name__)

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
        categories = ['Ocio', 'Comida', 'Servicios']
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
    
@app.route('/', methods=['GET', 'POST'])
def home():
    # Crear instancia de ExpensesTracker
    tracker = ExpensesTracker()
    
    if request.method == 'POST':
        amount = int(request.form['amount'])
        category = request.form['category']
        tracker.add_expense(amount, category)
    
    # Agregar gastos de ejemplo
    tracker.add_expense(50, 'Comida')
    tracker.add_expense(30, 'Ocio')
    tracker.add_expense(20, 'Servicios')
    
    # Obtener los gastos por categoría
    categories = ['Ocio', 'Comida', 'Servicios']
    expenses_by_category = [len(tracker.get_expenses_by_category(category)) for category in categories]
    
    # Generar gráfico de barras
    plt.bar(categories, expenses_by_category)
    plt.xlabel('Categorías')
    plt.ylabel('Cantidad de Gastos')
    plt.title('Gastos por Categoría')
    plt.savefig('static/graph.png')  # Guardar el gráfico como imagen
    
    # Obtener el reporte de gastos
    reporte = tracker.generate_report()
    
    return render_template('index.html', reporte=reporte)

if __name__ == '__main__':
    app.run()
