

import tkinter as tk
from tkinter import *

import browse_gui


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master = master
        self.master.resizable(width=False, height=False)
        # self.master.geometry("{}x{}".format(700, 400))
        self.master.geometry()
        self.master.title("Check Files")
        self.master.config(bg="lightgrey")

        browse_gui.load_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()