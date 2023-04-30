import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math
from Calculator import Calculator

window = tk.Tk()
window.title('Calculator')

frame = tk.Frame(master=window, bg="green", padx=10)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


def myclick(number):
    entry.insert(tk.END, number)


def equal():
    try:
        entry.delete(0, tk.END)
        entry.insert(0, str(eval(entry.get())))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
    entry.delete(0, tk.END)

column_gen = (j for k in range(1,4) for j in range(3))
for i in range(10):
    exec(f"button{i} = tk.Button(master=frame, text='{i}', padx=15, pady=5, width=3, command=lambda: myclick({i}))")
    if i == 0:
        continue
    exec(f"button{i}.grid(row={math.ceil(i/3)}, column={next(column_gen)}, padx=2, pady=2)")
button0.grid(row=4, column=1, padx=2, pady=2)
button_float = tk.Button(master=frame, text='.', padx=15, pady=5, width=3, command=lambda: myclick('.'))
button_float.grid(row=4, column=2, pady=2)

symbols = {'add': '+','sub': '-','mul': '*','div': '/'}
for k, v in symbols.items():
    exec(f'button_{k} = tk.Button(master=frame, text= "{v}", padx=15, pady=5, width=3, command=lambda: myclick("{v}"))')
    exec(f'button_{k}.grid(row={list(symbols.keys()).index(k)+2}, column=3, padx=2, pady=2)')

# clear button to clear the entry
button_clear = tk.Button(master=frame, text="C", padx=15, pady=5, width=3, command=clear)
button_clear.grid(row=1, column=3, pady=2)

# equal button to initialize operation
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, command=equal)
button_equal.grid(row=4, column=0, pady=2)


window.mainloop()
