import tkinter as tk
from menu  import menu

class OwnStart:
    def __init__(self,window):
	    self.window = window

    def window_init(self):
        self.window.title("own editor")
        self.window.geometry("600x600")

    def add_menu(self):
        menubar = tk.Menu(self.window)
        menu_add = menu.Menu(menubar)
        menu_add.create_menu()

    def add_text(self):
        text = tk.Text(self.window)
        text.pack(expand='yes',fill='both')

    def start(self):
        self.window_init()
        self.add_menu()
        self.add_text()
