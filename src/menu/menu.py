
import tkinter as tk
# from . import menuConfig
from . import fileMethods
class Menu:

    def __init__(self,window):
        self.window = window
        self.__create__menus(self.window)

    def __del__(self):
        pass

    def __inti_file_menu(self):
        pass

    def __create__menus(self,window):

        root_menu = tk.Menu(self.window,tearoff=0)
        fileMethods.fileOperator(root_menu,self.window)
        self.window.config(menu=root_menu)
