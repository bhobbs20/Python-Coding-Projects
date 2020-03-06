
import os
import sqlite3
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import gui_main
import shutil
import time


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

        # vars
        self.txt_files_one = StringVar()
        self.txt_files_two = StringVar()

        # Btn one: browse files from source directory
        self.btn_browse = Button(self.master, text="Source Directory:\nBrowse All Files", width=13, height=2,
                                 command=lambda: files(self))
        self.btn_browse.grid(row=4, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

        # Entry box one: for selected file
        self.txt_field_one = Entry(self.master, text=self.txt_files_one, font=("Helvetica", 16), fg='black', bg='white', width=37)
        self.txt_field_one.grid(row=4, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

        # Btn two: destination directory
        self.btn_browse_two = Button(self.master, text="Destination\nDirectory", width=13, height=2,
                                     command=lambda: get_file(self))
        self.btn_browse_two.grid(row=5, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

        # Entry box two: for destination file path
        self.txt_field_two = Entry(self.master, text=self.txt_files_two, fg='black', bg='white', width=37)
        self.txt_field_two.grid(row=5, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

        # Btn Des: trigger dest func
        self.btn_browse_txt = Button(self.master, text="Move .txt Files", width=14, height=2,
                                     command=lambda: destination(self))
        self.btn_browse_txt.grid(row=7, column=2, padx=(20, 100), pady=(100, 60), sticky=S)

        # Btn close: close program
        self.btn_cancel = tk.Button(self.master, width=12, height=2, text='Close Program', bg="lightgrey",
                                    command=self.cancel)
        self.btn_cancel.grid(row=7, column=3, padx=(0, 30), pady=(40, 40))

        # Select files from source directory and destination directory
        def files(self):
            self.txt_files_one.set(filedialog.askdirectory())

        def get_file(self):
            self.txt_files_two.set(filedialog.askdirectory())

        # Loop through files
        def destination(self):
            self.source_directory = self.txt_files_one.get()
            self.destination_directory = self.txt_files_two.get()
            self.files = os.listdir(self.source_directory)
            for files in self.files:
                if files.endswith(".txt"):
                    self.absolute_path = os.path.join(self.source_directory, files)
                    shutil.move(self.absolute_path, self.destination_directory)
                database(self)

        # creates db with txt files and time stamp
        def database(self):
            conn = sqlite3.connect('tkinter_txt_data.db')

            with conn:
                curr = conn.cursor()
                curr.execute("CREATE TABLE IF NOT EXISTS tbl_txt_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_txt_file TEXT, \
                    col_time_stamp TIMESTAMP \
                    );")

                conn.commit()
            conn.close()

            conn = sqlite3.connect('tkinter_txt_data.db')

            with conn:
                curr = conn.cursor()
                self.files = os.listdir(self.destination_directory)
                #  time stamp
                for files in self.files:
                    self.file_path = os.path.join(self.destination_directory, files)
                    curr.execute("INSERT INTO tbl_txt_files (col_txt_file , col_time_stamp) VALUES (?,?)",
                                 (files, (os.path.getmtime(self.file_path))), )
                    print(self.file_path, (os.path.getmtime(self.file_path)))

                conn.commit()
            conn.close()

    # close program
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

