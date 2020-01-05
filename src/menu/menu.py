import tkinter as tk
from . import menuName

class Menu:
    def __init__(self,window):
        self.window = window
        self.__create__menus(self.window)

    def __del__(self):
        pass

    def __test(self):
        pass
    def __create__menus(self,window):

        root_menu = tk.Menu(self.window,tearoff=0)
        # file_menu = tk.Menu(root_menu,tearoof=0)
        for rootMenu in menuName.datalist['rootMenu']:
            add_menu = tk.Menu(root_menu,tearoff=0)

            for secLevel in menuName.datalist[rootMenu]:
                add_menu.add_command(label=secLevel,command=self.__test)

            root_menu.add_cascade(label=rootMenu,menu=add_menu)

        self.window.config(menu=root_menu)
    
