import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        operation = entry_operation.get()
        num2 = float(entry_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        else:
            messagebox.showerror("Error", "Invalid operation. Please use +, -, *, or /")
            return

        label_result.config(text=f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_operation = tk.Label(root, text="Enter an operation (+, -, *, /):")
label_operation.pack()

entry_operation = tk.Entry(root)
entry_operation.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()