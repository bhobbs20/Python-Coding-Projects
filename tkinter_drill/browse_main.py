"""

Drill Description:
 Write a script that creates a GUI with
a button widget and a text widget.The script will also include a function
that when it is called will invoke a dialog modal which will allow users with
the ability to select a folder directory from their system. Finally, your
script will show the user’s selected directory path into the text field.

Requirements:
Your script will need to use Python 3 and the Tkinter module.

Your script will need to use the askdirectory() method from the Tkinter module.

Your script will need to have a function linked to the button widget so that once the button has been clicked will take the user’s selected file path retained by the askdirectory() method and print it within your GUI’s text widget.

"""

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
