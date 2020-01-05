import tkinter as tk
from menu import menu
class Own():
    def __init__(self):
        #create windows
        self.window = tk.Tk()
        self.__create__menus(self.window)
        self.__window_config(self.window)

        self.window.mainloop()

    def __del__(self):
        self.window

    def __window_config(self,window):
        window.title("Own")
        window.geometry("800x600")


    def __create__menus(self,window):
        menu.Menu(window)
