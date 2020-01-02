import tkinter as tk
import start

def main():
    window = tk.Tk()

    own = start.OwnStart(window)
    own.start()

    window.mainloop()

if __name__ == '__main__':
	main()
