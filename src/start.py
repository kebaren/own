import tkinter as tk

import menu as menu

class OwnStart:
    def __init__(self):
	    pass

    def create_window(self):
        window = tk.Tk()
        window.title("OWN")
        # window.wm_iconbitmap("own.ico")
        window.geometry("800x600")
        window.mainloop()

    def start(self):
        self.create_window()
        menu.
