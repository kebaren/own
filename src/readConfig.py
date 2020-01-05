import json
import os


class readConfig:

    def __init__(self):



    def __read_json_config(self,file_name):
        if os.path.exists(file_name):
            if os.path.getsize(file_name):
                with open(file_name,"r",encoding="utf-8") as fm:
                    data = json.load(fm)
                    fw.flush()
                    fw.close()
                    return data
            else:
                __write_json_config(filename,.datalist)
        else:
            __write_json_config(filename,self.datalist)

    def __write_json_config(self,file_name,datalsit):
        with open(file_name,"w",encoding="utf-8") as fw:
            fw.write(datalist)
            fw.flush()
            fw.close()

    def read_menu_name(self):
        file_name = "./config/menuName.json"
        self.__read_json_config(file_name)
