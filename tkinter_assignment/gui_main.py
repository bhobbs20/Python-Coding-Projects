
import os
from tkinter import *
import tkinter as tk
import main


def display_gui(self):


    # Btn close: close program
    self.btn_cancel = tk.Button(self.master, width=12, height=2, text='Close Program', bg="lightgrey",
                                command=self.cancel)
    self.btn_cancel.grid(row=7, column=3, padx=(0, 30), pady=(40, 40))


if __name__ == "__main__":
    pass

