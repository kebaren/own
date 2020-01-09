import tkinter as tk
from menu import menu
from text import text
import os
from PIL import Image
from PIL import ImageTk
class Own():
    def __init__(self):
        #create windows
        self.window = tk.Tk()
        self.__create__menus(self.window)
        self.__window_config(self.window)
        self.__create_text(self.window)

        self.window.mainloop()

    def __del__(self):
        self.window

    def __window_config(self,window):
        window.title("Own")
        window.geometry("800x600")
        img = ImageTk.PhotoImage(file="own.ico")
        window.tk.call('wm','iconphoto',window._w,img)


    def __create__menus(self,window):
        menu.Menu(self.window)

    def __create_text(self,window):
        text.textOperator(self.window)
