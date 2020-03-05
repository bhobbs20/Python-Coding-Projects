

from tkinter import *
# from tkinter import filedialog
import tkinter as tk
import gui_main
# import func_main


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry()
        self.master.title("Tkinter App")
        self.master.config(bg="lightgrey")

        # display view
        gui_main.display_gui(self)

    # FUNCTIONS
    # close program

    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

