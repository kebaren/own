import tkinter as tk
from . import file
import readConf as rc
class Menu:
    def __init__(self,root):
        self.root = root

    def __del__(self):
        self.root

    def init_menu(root):
        main_menu =tk.Menu(root)
        add_menu = tk.Menu(main_menu)
        data = rc.ReadMenuName.read_menu_name()

        for menu_value in data["main_menu"]:
            for val in data[menu_value]:
                
            main_menu.add_command(label=menu_value)
            # for val in data[menu_value]:
            #     add_menu.add_command(label=val,command=file.File.new_file)
        # for va in data['File']:
        #     add_menu.add_command(label=va)
        lista = ["新建","打开","复制","退出"]
        for item in lista:
            add_menu.add_command(label=item)

        main_menu.add_cascade(label='File',menu=add_menu)
        # root['menu'] = main_menu
        root.config(menu=main_menu)




    # def add_file_menu():
    #     pass
    #
    # def add_edit_menu():
    #     pass
    #
    # def add_view_menu():
    #     pass
    #
    # def add_selection_menu():
    #     pass
    #
    # def add_find_menu():
    #     pass
    #
    # def add_package_menu():
    #     pass
    #
    # def add_help_menui():
    #     pass
