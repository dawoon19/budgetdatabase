from tkinter import *
import sqlite3 as sql

class Home(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        #fonts
        headlinef = ("Avenir Next Condensed", 50, "bold")
        subheadf = ("Avenir Next Condensed", 20)
        buttonf = ("Avenir Next Condensed", 15, "bold")
        creditf = ("Avenir Next Condensed", 10)

        #Welcome
        welcome = Label(self.master, text = "Budget Management",
                        font = headlinef,width = 50, height = 5, fg = "#E3BC2D", bg = "#000000")
        welcome.pack()

        #Create Group Frame
        create_frm = Frame()
        create_frm.pack(padx = 20, pady = 20)
        create_group_btn = Button(create_frm, text = "C R E A T E   A   G R O U P",
                                  font = buttonf, width = 25, height = 2, fg = "#000000", bg = "#E3BC2D")
        create_group_btn.grid(row = 0, column = 0)

        #Existing Group Frame
        exist_frm = Frame()
        exist_frm.pack(padx = 20, pady = 20)
        exist_group_btn = Button(exist_frm, text = "S I G N   I N T O   E X I S T I N G   G R O U P",
                                 font = buttonf, width = 40, height = 2)
        exist_group_btn.grid(row = 0, column = 0)

        #Quit Button
        quit_frm = Frame()
        quit_frm.pack(padx = 20, pady = 20)
        quit_btn = Button(quit_frm, text = "Q U I T", font = buttonf, command = self.master.destroy, width = 20, height = 2)
        quit_btn.pack()

    def create_group(curr_wind):
        curr_wind.destroy()
        window

homepage = Home()
homepage.master.title("Budget Management")

mainloop()


