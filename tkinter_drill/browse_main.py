

import tkinter as tk
from tkinter import *


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

        self.btn_browse_1 = tk.Button(self.master, width=12, height=1, text='Browse', bg="lightgrey", highlightbackground='lightgrey')
        self.btn_browse_1.grid(row=0, column=1, padx=(30, 0), pady=(50, 0), sticky=E)

        self.txt_browse_file_1 = tk.Entry(self.master, text='')
        self.txt_browse_file_1.grid(row=0, column=2, rowspan=1, columnspan=9, padx=(30, 40), pady=(50, 0), sticky=N + E + W)

        self.btn_browse_2 = tk.Button(self.master, width=12, height=1, text='Browse', bg="lightgrey", highlightbackground='lightgrey')
        self.btn_browse_2.grid(row=1, column=1, padx=(30, 0), pady=(5, 0), sticky=E)

        self.txt_browse_file_1 = tk.Entry(self.master, text='')
        self.txt_browse_file_1.grid(row=1, column=2, rowspan=1, columnspan=9, padx=(30, 40), pady=(5, 0), sticky=N + E + W)

        self.btn_check_files = tk.Button(self.master, width=12, height=1, text='Check Files..', bg="lightgrey", highlightbackground='lightgrey')
        self.btn_check_files.grid(row=3, column=1, padx=(30, 0), pady=(40, 40), sticky=E)

        self.btn_cancel = tk.Button(self.master, width=12, height=1, text='Close Program', bg="lightgrey", highlightbackground='lightgrey')
        self.btn_cancel.grid(row=3, column=10, padx=(0, 30), pady=(40, 40))


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()