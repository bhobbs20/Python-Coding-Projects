

from tkinter import *
from tkinter import filedialog
import tkinter as tk


class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry()
        self.master.title("Tkinter App")
        self.master.config(bg="lightgrey")


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()