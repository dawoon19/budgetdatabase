from tkinter import *

class Page(Frame):
    def __init__(self, master=None, window=None,**kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.window = window
        self.config_size()
        self.bg_color = 'white'

    def create_title(self, title, font):
        title_lab = Label(self, text = title, font = font,
                          width = 30, height = 2, bg = self.bg_color)
        title_lab.grid(row = 0, column = 0,sticky = 'ew')

    def config_size(self):
        self.rowconfigure([0,1,2],weight = 1)
        self.columnconfigure(0,weight = 1)

class UserPage(Page):
    def __init__(self, master=None, window=None,**kwargs):
        Page.__init__(self, master, window,**kwargs)
        self.entries = []

    def go_home(self):
        self.master.reset_user()
        self.master.go_to(Home)
        for e in self.entries:
            e.delete(0,END)

class GroupPage(Page):
    def __init__(self, master = None, window = None, user = None, **kwargs):
        Page.__init__(self, master, window, **kwargs)
