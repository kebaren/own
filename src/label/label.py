import tkinter as tk

class labelCreate:
	def __init__(self,window):
		self.window = window
		# self.label = tk.Label(self.window,text="untitled")
		# self.label.pack(expand='yes',fill='y')
		default_name = "untitled"
		self.tab = tk.Button(self.window,text=default_name)
		self.tab.pack()