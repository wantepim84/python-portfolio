import tkinter as tk
from tkinter import messagebox

class BudgetTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker")

        self.expense_list = []

        tk.Label(root, text="Expense Description:").grid(
            row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Amount:").grid(row=1, column=0, padx=5, pady=5)

        self.expense_description_entry = tk.Entry(root)
        self.expense_description_entry.grid(row=0, column=1, padx=5, pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.show_button = tk.Button(
            root, text="Show Expenses", command=self.show_expenses)
        self.show_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_expense(self):
        description = self.expense_description_entry.get()
        amount = self.amount_entry.get()

        if description and amount:
            try:
                amount = float(amount)
                self.expense_list.append((description, amount))
                messagebox.showinfo("Success", "Expense added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Amount must be a number!")
        else:
            messagebox.showerror("Error", "Please fill in both fields!")

        self.expense_description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def show_expenses(self):
        total_expense = sum(amount for _, amount in self.expense_list)
        expense_text = "Expense List:\n\n"
        for description, amount in self.expense_list:
            expense_text += f"{description}: £{amount:.2f}\n"
        expense_text += f"\nTotal Expense: £{total_expense:.2f}"

        messagebox.showinfo("Expenses", expense_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()
