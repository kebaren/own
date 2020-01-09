import sys
sys.path.append("../")
import tkinter as tk
from tkinter import filedialog
import setup
from text import text
import readConfig

class fileOperator:
    def __init__(self,root_menu,window):
        self.window = window
        self.root_menu = root_menu
        self.file_menu = tk.Menu(self.root_menu,tearoff=0)
        self.__init_file_menu()

        self.root_menu.add_cascade(label="File",menu=self.file_menu)


    def __init_file_menu(self ):

        # menu_name =  readConfig.readConfig()
        # file_menu_name = menu_name.read_menu_name()
        # self.file_menu.add_command(label=file_menu_name['fileName'],command=self.__new_window,accelerator=file_menu_name['fileName']['New Window']['key'])
        # file_menu.add_command(label="New File",command=self.__new_file,accelerator="Ctrl+N")
        # file_menu.add_command(label="Open File",command=self.__open_file,accelerator="Ctrl+O")
        # file_menu.add_command(label="Open Folder...",command=self.__open_folder,accelerator="Ctrl+Shfit+O")
        # file_menu.add_command(label="Add Project Folder...",command=self.__add_project_folder,accelerator="Ctrl+Shfit+A")
        # reopen_projet_menu = tk.Menu(file_menu,tearoff=0)
        # file_menu.add_cascade(label="Reopen Project",menu=reopen_projet_menu)
        # file_menu.add_command(label="Reopen Last Item",command=self.__reopen_last_item,accelerator="Ctrl+Shfit+T")
        # file_menu.add_separator()
        # file_menu.add_command(label="Save",command=self.__save,accelerator="Ctrl+S")
        # file_menu.add_command(label="Save As...",command=self.__save_as,accelerator="Ctrl+Shfit+S")
        # file_menu.add_command(label="Save All",command=self.__save_all)
        # file_menu.add_separator()
        # file_menu.add_command(label="Close Tab",command=self.__close_tab,accelerator="Ctrl+W")
        # file_menu.add_command(label="Cl  ose Pane",command=self.__close_pane,accelerator="Ctrl+K,Ctrl+W")
        # file_menu.add_command(label="Close Window",command=self.__close_window,accelerator="Ctrl+Shfit+W")
        # file_menu.add_separator()
        # file_menu.add_command(label="Quit",command=self.__quit,accelerator="Ctrl+Q")
        # file_menu.add_command(label="Close All Tabs",command=self.__close_all_tab)
        # # file_menu.config(menu=reopen_projet_menu)

        # for val in file_menu_name['fileName']:
        #     self.file_menu.add_command(label=val,command=file_menu_name['fileName'][val]['func'],accelerator=file_menu_name['fileName'][val]['key'])
        #     print(file_menu_name['fileName'][val]['func'])
        #     # if val == "Add Project Folder":
        #     #     reopen_projet_menu = tk.Menu(self.file_menu,tearoff=0)
        #     #     self.file_menu.add_cascade(label="Reopen Project",menu=reopen_projet_menu)
        #     if val == "Reopen Last Item" or val == "Save All" or val == "Close Window":
        #         self.file_menu.add_separator()
        # self.file_menu.config(menu=reopen_projet_menu)






    def __new_window(self):
        setup.Own()
    def __new_file(self):
        pass
    def __open_file(self):
        pass
    def __open_folder(self):
        pass
    def __add_project_folder(self):
        pass
    def __reopen_project(self):
        pass
    def __reopen_last_item(self):
        pass
    def __save(self):
        text_entry = text.textOperator.get_text_entry(self.window)
        # file_save_name =
        file_name = filedialog.asksaveasfilename(title="untitled",defaultextension=".txt")
        with open(file_name,"w",encoding="utf-8") as fw:
            fw.write(text_entry)
            fw.flush()

    def __save_as(self):
        pass

    def __save_all(self):
        pass

    def __close_tab(self):
        pass

    def __close_pane(self):
        pass

    def __close_window(self):
        pass

    def __quit(self):
        self.window.quit()

    def __close_all_tab(self):
        pass
