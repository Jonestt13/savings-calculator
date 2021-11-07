from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Savings Calc")

total = Entry(root,bg="black", fg="white", bd=5)
total.pack()
total.insert(0, "total income: ")
expenses = Entry(root,bg="black", fg="white", bd=5 )
expenses.pack()
expenses.insert(0, "total expenses: ")
def save_15():
    stotal = (int(total.get()) - int(expenses.get())) * .15
    savings = Label(root, text=f"Put {stotal} into savings")
    savings.pack()

ttk.Label(root, text="Savings Calculator").pack()
execute_savings = Button(root, text="Calculate savings at 15%", command=save_15)
execute_savings.pack()

ttk.Button(root, text="EXIT", command=root.destroy).pack()

root.mainloop() 

