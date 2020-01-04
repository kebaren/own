
from tkinter import *


def print_hello():
    print('冬青,hello!')


def main():
    root = Tk()

    menubar = Menu(root)
    menubar.add_command(label='冬青',
                        command=print_hello)

    root.config(menu=menubar)

    mainloop()


if __name__ == '__main__':
    main()
