import tkinter as tk
from menu import menu
from text import text
from label import label
import os
from PIL import Image
from PIL import ImageTk
class Own():
    def __init__(self):
        #create windows
        self.window = tk.Tk()
        self.__create__menus()
        self.__window_config(self.window)
        self.__create_label()
        self.__create_text()

        self.window.mainloop()

    def __del__(self):
        self.window

    def __window_config(self,window):
        window.title("Own")
        window.geometry("800x600")
        img = ImageTk.PhotoImage(file="own.ico")
        window.tk.call('wm','iconphoto',window._w,img)


    def __create__menus(self):
    	self.menu =  menu.Menu(self.window)

    def __create_text(self):
    	self.text =   text.textOperator(self.window)

    def __create_label(self):
    	self.label = label.labelCreate(self.window)

    def __config__window(self):
    	pass