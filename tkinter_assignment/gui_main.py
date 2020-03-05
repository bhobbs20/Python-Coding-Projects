
import os
from tkinter import *
import tkinter as tk


def display_gui(self):
    # Vars
    self.txtFiles = StringVar()
    self.txtFiles_two = StringVar()

    # Btn one: browse files from source directory
    self.btn_browse = Button(self.master, text="Source Directory:\nBrowse All Files", width=13, height=2)
    self.btn_browse.grid(row=4, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

    # Entry box one: for selected file
    self.txt_field_one = Entry(self.master, text="box text1", font=("Helvetica", 16), fg='black', bg='white', width=37)
    self.txt_field_one.grid(row=4, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

    # Btn 2: destination directory
    self.btn_browse_two = Button(self.master, text="Destination\nDirectory", width=13, height=2)
    self.btn_browse_two.grid(row=5, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

    # Entry box two: for destination file path
    self.txt_field_two = Entry(self.master, text="file path", fg='black', bg='white',width=37)
    self.txt_field_two.grid(row=5, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

    # Btn three: browse .txt files
    self.btn_browse_txt = Button(self.master, text="Move .txt Files", width=14, height=2)
    self.btn_browse_txt.grid(row=7, column=2, padx=(20, 100), pady=(100, 60), sticky=S)

    # Btn close: close program
    self.btn_cancel = tk.Button(self.master, width=12, height=2, text='Close Program', bg="lightgrey",
                                command=self.cancel)
    self.btn_cancel.grid(row=7, column=3, padx=(0, 30), pady=(40, 40))


if __name__ == "__main__":
    pass

