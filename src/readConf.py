import json

class ReadMenuName:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def read_menu_name():
        with open("../config/menu_name.json","r",encoding="utf-8") as fw:
            data = json.load(fw)
        return data
