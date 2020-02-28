import tkinter as Tk
from tkinter import *


class ParentWindow(Tk.Frame):
    def __init__(self, master):
        Tk.Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('()x()'.format(700, 400))
        self.master.title("learning tkinter")


if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()