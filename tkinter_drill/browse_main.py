

from tkinter import *
from tkinter import filedialog
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry()
        self.master.title("Check Files")
        self.master.config(bg="lightgrey")

        # Button to fire dialog
        self.btn_browse_1 = tk.Button(self.master, width=12, height=1, text='Browse', bg="lightgrey",
                                      highlightbackground='lightgrey', command=self.find_directory)

        self.btn_browse_1.grid(row=0, column=1, padx=(30, 0), pady=(50, 0), sticky=E)

        # Show directory name here
        self.txt_browse_file_1 = tk.Entry(self.master, text='')
        self.txt_browse_file_1.grid(row=1, column=2, rowspan=1, columnspan=9, padx=(30, 40), pady=(50, 0),
                                    sticky=N + E + W)

        self.btn_browse_2 = tk.Button(self.master, width=12, height=1, text='Browse', bg="lightgrey",
                                      highlightbackground='lightgrey')
        self.btn_browse_2.grid(row=2, column=1, padx=(30, 0), pady=(5, 0), sticky=E)

        self.txt_browse_file_1 = tk.Entry(self.master, text='')
        self.txt_browse_file_1.grid(row=1, column=2, rowspan=1, columnspan=9, padx=(30, 40), pady=(5, 0),
                                    sticky=N + E + W)

        self.btn_check_files = tk.Button(self.master, width=12, height=1, text='Check Files..', bg="lightgrey",
                                         highlightbackground='lightgrey')
        self.btn_check_files.grid(row=3, column=1, padx=(30, 0), pady=(40, 40), sticky=E)

        self.btn_cancel = tk.Button(self.master, width=12, height=1, text='Close Program', bg="lightgrey",
                                    highlightbackground='lightgrey', command=self.cancel)
        self.btn_cancel.grid(row=3, column=10, padx=(0, 30), pady=(40, 40))

        self.var_directory_name = StringVar()

    # find directory function
    def find_directory(self):
        self.var_directory_name = tk.filedialog.askdirectory()
        self.txt_browse_file_1.insert(0, self.var_directory_name)
        self.txt_browse_file_1.config(text="{}".format(self.var_directory_name))

    # This works
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
