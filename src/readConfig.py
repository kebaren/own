import json
import os
import tkinter as tk

class readConfig:

    def __init__(self):
        pass

    def __read_json_config(self,file_name):
        if os.path.exists(file_name):
            if os.path.getsize(file_name):
                with open(file_name,"r",encoding="utf-8") as fm:
                    data = json.load(fm)
                    fm.close()
                    return data
            else:
                tk.messagebox.showerror(title="error!",text="configure file is emptry!")
        else:
            tk.messagebox.showerror(title="error!",text="configre file does not exists!")

    def read_menu_name(self):
        file_name = "./config/menuName.json"
        file_menu = self.__read_json_config(file_name)
        return file_menu
