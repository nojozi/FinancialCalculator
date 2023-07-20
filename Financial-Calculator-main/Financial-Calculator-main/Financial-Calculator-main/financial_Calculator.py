import tkinter as tk
import math
from tkinter import RIDGE

from param.ipython import blue

# Create GUI
root = tk.Tk()
# top = tk.Tk()
root.geometry("")

root.title("Investment Calculator by The Winning Team")
root.configure(bg="grey")

frame1 = tk.Frame(root, width=600, height=250, highlightbackground="blue", highlightthickness=5)
# frame1.grid(row=15, column=15, padx=5, pady=5)

text_bg_color = "black"
# Create labels and entries for investment calculation
inv_label = tk.Label(root, text="Investment Calculator", font=("Times New Roman", 16, "bold"))
inv_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

inv_amount_label = tk.Label(root, text="Principal Amount:", font=("Times New Roman", 13))
inv_amount_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")
inv_amount_entry = tk.Entry(root, font=("Times New Roman", 13))
inv_amount_entry.grid(row=1, column=1, padx=10, pady=5)

inv_rate_label = tk.Label(root, text="Interest rate (%):", font=("Times New Roman", 13))
inv_rate_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")
inv_rate_entry = tk.Entry(root, font=("Times New Roman", 13))
inv_rate_entry.grid(row=2, column=1, padx=10, pady=5)

inv_time_label = tk.Label(root, text="Given Years:", font=("Times New Roman", 13))
inv_time_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")
inv_time_entry = tk.Entry(root, font=("Times New Roman", 13))
inv_time_entry.grid(row=3, column=1, padx=10, pady=5)

inv_interest_label = tk.Label(root, text="Interest type:", font=("Times New Roman", 13))
inv_interest_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")
inv_interest_var = tk.StringVar(value="Simple")
inv_interest_simple = tk.Radiobutton(root, text="Simple interest", font=("Times New Roman", 13), variable=inv_interest_var, value="Simple")
inv_interest_simple.grid(row=4, column=1, padx=10, pady=5, sticky="W")
inv_interest_compound = tk.Radiobutton(root, text="Compound interest", font=("Times New Roman", 12), variable=inv_interest_var, value="Compound")
inv_interest_compound.grid(row=5, column=1, padx=10, pady=5, sticky="W")

inv_answer_label = tk.Label(root, text="", font=("Times New Roman", 12, "bold"), fg="red")
inv_answer_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def calculate_investment():
    inv_amount = float(inv_amount_entry.get())
    inv_rate = float(inv_rate_entry.get())
    inv_time = int(inv_time_entry.get())
    interest_type = inv_interest_var.get()

    if interest_type == "Simple":
        inv_answer = inv_amount * (1 + (inv_rate / 100) * inv_time)
    elif interest_type == "Compound":
        inv_answer = inv_amount * math.pow((1 + inv_rate / 100), inv_time)

    inv_answer_label.config(text=f"Your investment will be worth R{inv_answer:.2f}.")

inv_button = tk.Button(root, text="Calculate Investment", font=("Times New Roman", 13), command=calculate_investment)
inv_button.grid(row=7, column=0, padx=10, pady=10)
def clear_investment():
    inv_amount_entry.delete(0, tk.END)
    inv_rate_entry.delete(0, tk.END)
    inv_time_entry.delete(0, tk.END)
    inv_answer_label.config(text="")

clear_inv_button = tk.Button(root, text="Clear Investment", font=("Times New Roman", 13), command=clear_investment)
clear_inv_button.grid(row=7, column=1, padx=10, pady=10)
# Create labels and entries for bond calculation
bond_label = tk.Label(root, text="Bond Calculator", font=("Times New Roman", 16, "bold"))
bond_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

bond_value_label = tk.Label(root, text="Present value of the house:", font=("Times New Roman", 13))
bond_value_label.grid(row=1, column=2, padx=10, pady=5, sticky="W")
bond_value_entry = tk.Entry(root, font=("Times New Roman", 13))
bond_value_entry.grid(row=1, column=3, padx=10, pady=5)

bond_rate_label = tk.Label(root, text="Interest rate (%):", font=("Times New Roman", 13))
bond_rate_label.grid(row=2, column=2, padx=10, pady=5, sticky="W")
bond_rate_entry = tk.Entry(root, font=("Times New Roman", 13))
bond_rate_entry.grid(row=2, column=3, padx=10, pady=5)

bond_time_label = tk.Label(root, text="Given Years:", font=("Times New Roman", 13))
bond_time_label.grid(row=3, column=2, padx=10, pady=5, sticky="W")
bond_time_entry = tk.Entry(root, font=("Times New Roman", 13))
bond_time_entry.grid(row=3, column=3, padx=10, pady=5)

bond_answer_label = tk.Label(root, text="", font=("Times New Roman", 13, "bold"), fg="red")
bond_answer_label.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

def calculate_bond():
    bond_value = float(bond_value_entry.get())
    bond_rate = float(bond_rate_entry.get())
    bond_time = int(bond_time_entry.get())
    bond_payment = bond_value / (((1 - math.pow((1 + bond_rate / 100), -bond_time))) / (bond_rate / 100))
    bond_answer_label.config(text=f"Your monthly payment will be R{bond_payment:.2f}.")

bond_button = tk.Button(root, text="Calculate Bond", font=("Times New Roman", 13), command=calculate_bond)
bond_button.grid(row=7, column=2, padx=10, pady=10)
def clear_bond():
    bond_value_entry.delete(0, tk.END)
    bond_rate_entry.delete(0, tk.END)
    bond_time_entry.delete(0, tk.END)
    bond_answer_label.config(text="")

clear_bond_button = tk.Button(root, text="Clear Bond", font=("Times New Roman", 13), command=clear_bond)
clear_bond_button.grid(row=7, column=3, padx=10, pady=10)

root.mainloop()


