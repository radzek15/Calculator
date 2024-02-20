import tkinter as tk

from .constants import *


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(APP_TITLE)
        self.entered_string = tk.StringVar()
        self.memory = 0
        self.entry = tk.Entry(
            self.window,
            textvariable=self.entered_string,
            width=18,
            font=("Calibri", 28),
            state="readonly",
            justify="right",
        )
        self.entry.grid(row=1, column=1, columnspan=4)

        self.buttons = {
            0: [7, 2, lambda: self.on_button_click(0)],
            1: [6, 1, lambda: self.on_button_click(1)],
            2: [6, 2, lambda: self.on_button_click(2)],
            3: [6, 3, lambda: self.on_button_click(3)],
            4: [5, 1, lambda: self.on_button_click(4)],
            5: [5, 2, lambda: self.on_button_click(5)],
            6: [5, 3, lambda: self.on_button_click(6)],
            7: [4, 1, lambda: self.on_button_click(7)],
            8: [4, 2, lambda: self.on_button_click(8)],
            9: [4, 3, lambda: self.on_button_click(9)],
            "+": [6, 4, lambda: self.on_button_click("+")],
            "-": [5, 4, lambda: self.on_button_click("-")],
            "*": [4, 4, lambda: self.on_button_click("*")],
            "/": [3, 4, lambda: self.on_button_click("/")],
            "=": [7, 4, lambda: self.on_button_click("=")],
            ".": [7, 3, lambda: self.on_button_click(".")],
            "+/-": [7, 1, lambda: self.negate()],
            "C": [3, 3, lambda: self.erase_button_click()],
            "M+": [2, 3, lambda: self.add_to_memory()],
            "Mr": [2, 1, lambda: self.load_memory()],
            "Mc": [2, 2, lambda: self.erase_memory()],
        }

        self.operations = {
            "+/-": (7, 1),
            "=": (7, 4),
            "^": (3, 1),
            "\u221A": (3, 2),
        }

    @staticmethod
    def change_state_decorator(func):
        def change_state_wrapper(self, *args, **kwargs):
            self.entry.config(state="normal")
            func(self, *args, **kwargs)
            self.entry.config(state="readonly")

        return change_state_wrapper

    def place_buttons(self):
        for num, [row, col, command] in self.buttons.items():
            btn = tk.Button(self.window, text=str(num), width=10, height=3, command=command)
            btn.grid(row=row, column=col)

    def run(self):
        self.window.mainloop()

    @change_state_decorator
    def on_button_click(self, value):
        self.entry.insert(tk.END, str(value))

    @change_state_decorator
    def erase_button_click(self):
        self.entry.delete(0, tk.END)

    def add_to_memory(self):
        try:
            self.memory += float(self.entered_string.get())
        except ValueError:
            pass

    def erase_memory(self):
        self.memory = 0

    @change_state_decorator
    def load_memory(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(self.memory))

    @change_state_decorator
    def negate(self):
        old_value = float(self.entered_string.get())
        negated_value = -old_value
        self.entered_string.set(str(negated_value))
