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
            font=FONT,
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
            "=": [7, 4, lambda: self.on_equal_sign_click()],
            ".": [7, 3, lambda: self.on_button_click(".")],
            "+/-": [7, 1, lambda: self.negate()],
            "(": [3, 1, lambda: self.on_button_click("(")],
            ")": [3, 2, lambda: self.on_button_click(")")],
            "C": [3, 3, lambda: self.clear_button()],
            "Ms": [2, 1, lambda: self.memory_store()],
            "M+": [2, 2, lambda: self.memory_add()],
            "Mc": [2, 3, lambda: self.memory_clear()],
            "Mr": [2, 4, lambda: self.memory_recall()],
            # "\u221A"
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
        numbers = set(range(10))
        operators = {"+", "-", "*", "/", "."}
        current_text = self.entered_string.get()

        if not current_text and value in operators:
            pass
        elif current_text == "0" and value in numbers:
            self.entered_string.set(value)
        elif current_text and current_text[-1] in operators and value in operators:
            self.entered_string.set(current_text[:-1] + value)
        else:
            self.entered_string.set(current_text + str(value))

    @change_state_decorator
    def clear_button(self):
        self.entered_string.set("")

    def memory_add(self):
        try:
            self.memory += float(self.entered_string.get())
        except ValueError:
            pass

    def memory_clear(self):
        self.memory = 0

    @change_state_decorator
    def memory_recall(self):
        self.entered_string.set(str(self.memory))

    def memory_store(self):
        self.memory_clear()
        self.memory_add()

    @change_state_decorator
    def negate(self):
        old_value = float(self.entered_string.get())
        negated_value = -old_value
        self.entered_string.set(str(negated_value))

    @change_state_decorator
    def on_equal_sign_click(self):
        expression = self.entered_string.get()
        try:
            evaluated = eval(expression)
            self.entered_string.set(str(evaluated))
        except SyntaxError or TypeError:
            pass
