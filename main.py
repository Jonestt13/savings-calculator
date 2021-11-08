from re import L
from tkinter import *
from tkinter import ttk
from tkcalendar import *

root = Tk()
root.title("Savings Calc")

cal = Calendar(root, selectmode="day", year=2021, month=11, day=1)
cal.pack()

total = Entry(root,bg="black", fg="white", bd=5)
total.pack()
total.insert(0, "total income: ")
expenses = Entry(root,bg="black", fg="white", bd=5 )
expenses.pack()
expenses.insert(0, "total expenses: ")
def save_5():
    stotal = (int(total.get()) - int(expenses.get())) * .05
    savings = Label(root, text=f"Put {stotal} into savings")
    savings.pack()
def save_15():
    stotal = (int(total.get()) - int(expenses.get())) * .15
    savings = Label(root, text=f"Put {stotal} into savings")
    savings.pack()
def save_20():
    stotal = (int(total.get()) - int(expenses.get())) * .20
    savings = Label(root, text=f"Put {stotal} into savings")
    savings.pack()
def select_date():
    date_selected.config(text=cal.get_date())

date = Button(root, text="select date", command=select_date)
date.pack()
date_selected = Label(root, text='')
date_selected.pack()

ttk.Label(root, text="Savings Calculator").pack()
savings_5 = Button(root, text="Calculate savings at 5%", command=save_5)
savings_5.pack()
savings_15 = Button(root, text="Calculate savings at 15%", command=save_15)
savings_15.pack()
savings_20 = Button(root, text="Calculate savings at 20%", command=save_20)
savings_20.pack()

ttk.Button(root, text="EXIT", command=root.destroy).pack(side=BOTTOM)

root.mainloop() 

