from tkinter import PhotoImage

from src.constants import APP_ICON
from src.Gui import Gui

if __name__ == "__main__":
    calc = Gui()
    calc.window.iconphoto(False, PhotoImage(file=APP_ICON))
    calc.place_buttons()
    calc.run()
