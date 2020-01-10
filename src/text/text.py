import tkinter as tk
from tkinter import scrolledtext
class textOperator():

    text = ''
    # textEntry = ''

    def __init__(self,window):
        self.window = window
        self.__init_text(self.window)
        # self.__add_scroball()

    def __init_text(self,window):
       
        global text
        text  = scrolledtext.ScrolledText(self.window)
        text.pack(expand="yes",fill="both")
        

    # def __add_scroball(self):
    #     global text
    #     scro = tk.Scrollbar(text,orient = "horizontal")
    #     scro.pack(expand="yes",fill="x",side="bottom")

    def get_text_entry(self):
        global text
        return text.get("0.0","end")

    def return_text_entry(self,varytext):
        global text
        text.insert("insert",varytext)

