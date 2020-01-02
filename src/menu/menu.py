import tkinter as tk
from menu import file
import readConf as rc
class Menu:
    def __init__(self,main_menu):
        self.main_menu = main_menu

    def __del__(self):
        self.main_menu

    def create_menu(self):
        menu_bar = tk.Menu(self.main_menu)
        # other_menu = rc.ReadMenuName.read_menu_name()['File']
        # for i in other_menu:
        self.main_menu.add_cascade(label='File',menu=menu_bar)

        # for index1 in other_menu:
        #     self.main_menu.add_command(index1)
        #     for index2 in other_menu[' ']:
        #         menu_bar.add_command(self.main_menu,label=(index2+other_menu[' '][index2]))
        #








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
