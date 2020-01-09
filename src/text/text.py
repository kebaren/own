import tkinter as tk
class textOperator():

    text = None

    def __init__(self,window):
        self.window = window
        self.__init_text(self.window)

    def __init_text(self,window):
        global text
        text  = tk.Text(self.window)
        text.pack(expand="yes",fill="both")

    def get_text_entry(self):
        global text
        return text.get("0.0","end")
