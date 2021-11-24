from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from individual_user import *
from passwordencrypt import encrypt
import sqlite3 as sql

class App(Frame):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.grid(row = 0, column = 0, sticky = NSEW)

        self.window = master

        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight = 1)

        self.pages = {}

        #general start pages
        for p in [Home, CreateUser, ExistUser]:
            new_page = p(self, self.window)
            self.pages[p] = new_page
            new_page.grid(row = 0, column = 0, sticky = NSEW)
        
        self.go_to(Home)

    def go_to(self, next_page_class):
        curr_page = self.pages[next_page_class]
        curr_page.refocus()
        curr_page.tkraise()

    def create_pages(self, page_class):
        new_page = page_class(self, self.window)
        self.pages[page_class] = new_page
        new_page.grid(row = 0, column = 0, sticky = NSEW)

#Base Page Classes
class Page(Frame):
    def __init__(self, master=None, window=None,**kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.window = window
        self.config_size()
        self.bg_color = 'white'
        self.first_entry = None

    def refocus(self):
        if self.first_entry!=None:
            self.first_entry.focus()

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
        self.master.go_to(Home)
        for e in self.entries:
            e.delete(0,END)

class GroupPage(Page):
    curr_user = User('FirstName', 'LastName', 'username', 'password')
    
    def __init__(self, master = None, window = None, **kwargs):
        Page.__init__(self, master, window, **kwargs)

    @classmethod
    def update_user(cls, user):
        GroupPage.curr_user = user

    @classmethod
    def reset_user(cls):
        GroupPage.curr_user = User('FirstName', 'LastName', 'username', 'password')

    def log_out(self):
        GroupPage.reset_user()
        self.master.go_to(Home)

#Start Pages
class Home(Page):
    def __init__(self, master=None, window=None,**kwargs):
        Page.__init__(self, master, window, **kwargs)
        self.bg_color = '#d3e0e0'
        self['bg'] = self.bg_color
        
        self.create_title('B U D G E T   D A T A B A S E', ('DIN Condensed', 60, 'bold'))
        
        login_frame = Frame(self,borderwidth = 2, bg = '#ebf4f5', highlightbackground = 'white', highlightthickness = 1)
        login_frame.grid(row = 1, column = 0, ipadx = 15, ipady = 30)
        login_frame.rowconfigure([0,1,2,3],weight = 3)
        login_frame.grid_columnconfigure(0,weight = 1)

        new_user_lab = Label(login_frame, text = 'New to Budget Database?',
                                 font = ('Avenir Next Condensed',15),bg = '#ebf4f5')
        new_user_lab.grid(row = 0, column = 0, sticky = S)

        new_user_b = Button(login_frame, text = 'Create New User...',font = ('DIN Condensed',18,'bold'),
                            width = 15,borderwidth = 0,command = lambda:self.master.go_to(CreateUser))
        new_user_b.grid(row = 1, column = 0,ipadx = 10, ipady = 5, sticky = N)

        new_user_lab = Label(login_frame, text = 'Already have a profile?',
                                 font = ('Avenir Next Condensed',15),bg = '#ebf4f5')
        new_user_lab.grid(row = 2, column = 0, sticky = S)
        
        old_user_b = Button(login_frame, text = 'Sign In',font = ('DIN Condensed',18,'bold'),
                            width = 15, command = lambda:self.master.go_to(ExistUser))
        old_user_b.grid(row = 3, column = 0, ipadx = 5, ipady = 5, sticky = N)

        quit_b = Button(self, text = 'Quit Program', font = ('DIN Condensed',18,),command=self.window.destroy)
        quit_b.grid(row = 2, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30, sticky = S)

class CreateUser(UserPage):
    def __init__(self, master=None, window=None, **kwargs):
        UserPage.__init__(self, master, window, **kwargs)

        self.input_frame = Frame(self)
        self.input_frame.grid(row = 1, column = 0, ipadx = 15, sticky = N)

        #Boolean values to check submission requirements
        self.name_reqs = [False, False, False] #Index 0: first name, Index 1: last name, Index 2: username
        self.char_req_pass = False
        self.num_req_pass = False
        
        #First Name Input
        fname_lab = Label(self.input_frame, text = 'First Name', font = ('Avenir Next Condensed',15))
        fname_ent = Entry(self.input_frame, relief = FLAT)
        fname_check = Label(self.input_frame, text = 'Must be at least 2 characters.', font = ('Avenir Next Condensed', 12))
        fname_lab.grid(row=0, column = 0, sticky = 'e')
        fname_ent.grid(row = 0, column = 1)
        fname_check.grid(row = 1, column = 1, sticky = 'w')
        self.first_entry = fname_ent

        #Last Name Input
        lname_lab = Label(self.input_frame, text = 'Last Name', font = ('Avenir Next Condensed',15))
        lname_ent = Entry(self.input_frame, relief = FLAT)
        lname_check = Label(self.input_frame, text = 'Must be at least 2 characters.', font = ('Avenir Next Condensed', 12))
        lname_lab.grid(row=2, column = 0, sticky = 'e')
        lname_ent.grid(row = 2, column = 1)
        lname_check.grid(row = 1, column = 1, sticky = 'w')

        #Username Input
        uname_lab = Label(self.input_frame, text = 'Enter Username', font = ('Avenir Next Condensed',15))
        uname_ent = Entry(self.input_frame, relief = FLAT)
        uname_check = Label(self.input_frame, text = 'Must be at least 5 characters.', font = ('Avenir Next Condensed', 12))
        uname_lab.grid(row=4, column = 0, sticky = 'e')
        uname_ent.grid(row = 4, column = 1)
        uname_check.grid(row = 5, column = 1, sticky = 'w')

        #Checking requirements for full name & username
        self.check_name_entry(fname_ent, fname_check, 2, 'f')
        self.check_name_entry(lname_ent, lname_check, 2, 'l')
        self.check_name_entry(uname_ent, uname_check, 5, 'u')

        #Password Input
        pass_lab = Label(self.input_frame, text = 'Enter Password', font = ('Avenir Next Condensed',15))
        pass_ent = Entry(self.input_frame, relief = FLAT, show = '*')
        pass_lab.grid(row=6, column = 0, sticky = 'e')
        pass_ent.grid(row =6, column = 1)

        #Checking requirements for password
        pass_check_char = Label(self.input_frame, text = 'Must be at least 8 characters.', font = ('Avenir Next Condensed', 12))
        pass_check_num = Label(self.input_frame, text = 'Must have at least 2 numbers.', font = ('Avenir Next Condensed', 12))
        pass_check_char.grid(row = 7, column = 1, sticky = 'w')
        pass_check_num.grid(row = 8, column = 1, sticky = 'w')

        self.check_pass_entry(pass_ent, pass_check_char, 'char')
        self.check_pass_entry(pass_ent, pass_check_num, 'num')

        #Submit Button
        submit_b = Button(self, text = 'Submit', command=self.submit, state = DISABLED)
        submit_b.grid(row = 2, column = 0, padx = 30, pady = 30, ipadx = 5, ipady = 5, sticky = 'ew')
        self.check_submit_req(submit_b)

        #Return to home button
        cancel_b = Button(self, text = 'Cancel', command=self.go_home)
        cancel_b.grid(row = 3, column = 0, padx = 30, pady = 30, ipadx = 5, ipady = 5, sticky = 'ew')

        self.entries = [fname_ent, lname_ent, uname_ent, pass_ent]

    def submit(self):
        fname_ent = self.entries[0].get()
        lname_ent = self.entries[1].get()
        uname_ent = self.entries[2].get()
        pass_ent = self.entries[3].get()
        
        answer = messagebox.askyesno('Confirmation', 'Is the information correct?')
        if answer == 1:
            conn = sql.connect('users.db')
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ?",(uname_ent,))
            records = c.fetchall()
            if len(records)>0:
                messagebox.showwarning('Username already exists',
                                       'This username has been taken.\nPlease use a different username.')
            else:
                encrypted = encrypt(uname_ent, pass_ent)
                c.execute("INSERT INTO users VALUES (:fname, :lname, :username, :password)",
                          {'fname': fname_ent,
                           'lname': lname_ent,
                           'username': uname_ent,
                           'password': encrypted
                           })
                conn.commit()
                update_USER_DATABASE()
                for u in USER_DATABASE:
                    if u.username == uname_ent:
                        GroupPage.curr_user = u
                self.master.create_pages(GroupHome)
                self.master.go_to(GroupHome)
            conn.commit()
            conn.close()

    def check_submit_req(self, button):
        reqs = self.name_reqs + [self.char_req_pass, self.num_req_pass]
        if all(reqs):
            button['state'] = NORMAL
        else:
            button['state'] = DISABLED
        self.after(100, lambda: self.check_submit_req(button))

    def check_name_entry(self, entry, label, min_chars, requirement):
        if requirement =='f':
            index = 0
        elif requirement == 'l':
            index = 1
        else:
            index = 2
            
        if len(entry.get())>=min_chars:
            entry.config(highlightbackground = '#dbdbdb')
            label.grid_forget()
            self.name_reqs[index]=True
        else:
            entry.config(highlightbackground = 'green')
            entry.config(highlightthickness = 1)
            label.grid(row = entry.grid_info()['row']+1, column = 1, sticky = 'w')
            self.name_reqs[index] = False
        self.after(100, lambda:self.check_name_entry(entry,label,min_chars,requirement))

    def check_pass_entry(self, entry, label, requirement):
        password = entry.get()
        if requirement == 'char':
            if len(entry.get())>=8:
                label.grid_forget()
                self.char_req_pass = True
            else:
                label.grid(row = entry.grid_info()['row']+1, column = 1, sticky = 'w')
                self.char_req_pass = False
        elif requirement =='num':
            number_count = 0
            for index in range(len(password)):
                try:
                    int(password[index])
                    number_count+=1
                except ValueError:
                    pass
            if number_count>=2:
                label.grid_forget()
                self.num_req_pass = True
            else:
                label.grid(row = entry.grid_info()['row']+2, column = 1, sticky = 'w')
                self.num_req_pass = False

        if self.num_req_pass and self.char_req_pass:
            entry.config(highlightbackground = '#dbdbdb')
        else:
            entry.config(highlightbackground = 'green')
            entry.config(highlightthickness = 1)

        self.after(100, lambda:self.check_pass_entry(entry,label,requirement))

    def check_username_entry(self, entry=None):
        error_lab = Label(self.input_frame, fg = 'red')
        error_lab.grid(row = entry.grid_info()['row']+1, column = 1)
        if len(entry.get())<5:
            error_lab['text']='Needs to be at least 5 characters'
        else:
            error_lab['text']=None

class ExistUser(UserPage):
    def __init__(self, master = None, window = None, **kwargs):
        UserPage.__init__(self, master, window, **kwargs)

        self.create_title('W E L C O M E   B A C K !',('DIN Condensed', 60, 'bold'))
        
        login_frame = Frame(self,borderwidth = 2, relief = RAISED)
        login_frame.grid(row = 1, column = 0, ipadx = 15, ipady = 15, sticky = N)

        name_lab = Label(login_frame, text = '\nUsername', font = ('Avenir Next Condensed', 15))
        name_ent = Entry(login_frame)
        name_lab.pack()
        name_ent.pack()
        self.first_entry = name_ent

        pass_lab = Label(login_frame, text = '\nPassword', font = ('Avenir Next Condensed', 15))
        pass_ent = Entry(login_frame, show = '*')
        pass_lab.pack()
        pass_ent.pack()

        submit_b = Button(login_frame, text = 'SUBMIT', font = ('DIN Condensed', 20), width = 20,
                          command = lambda: self.submit(name_ent.get(), pass_ent.get()))
        submit_b.pack(ipadx = 5, ipady = 5, padx = 15, pady = 15, side = 'bottom')
        
        cancel_b = Button(self, text = 'Cancel', command=self.go_home)
        cancel_b.grid(row = 2, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)

        self.entries = [name_ent, pass_ent]

    def submit(self, username, password):
        uname_ent = self.entries[0].get()
        pass_ent = self.entries[1].get()
        
        conn = sql.connect('users.db')
        c = conn.cursor()

        c.execute("SELECT username, password FROM users WHERE username = :uname",{'uname':uname_ent})
        records = c.fetchone()
        if records ==None:
            messagebox.showerror('User doesn\'t exist', 'This is not a valid username, please try again.')
        else:
            if encrypt(uname_ent, pass_ent) != records[1]:
                messagebox.showerror('Incorrect password', 'The password is incorrect. Try again.')
            else:
                for e in self.entries:
                    e.delete(0,END)
                for u in USER_DATABASE:
                    if u.username == uname_ent:
                        GroupPage.curr_user = u
                self.master.create_pages(GroupHome)
                self.master.go_to(GroupHome)
        
#User-Specific Pages
class GroupHome(GroupPage):
    def __init__ (self, master = None, window = None, **kwargs):
        GroupPage.__init__(self, master, window, **kwargs)
        self.user = GroupPage.curr_user
        
        self.create_title('Welcome, {}'.format(self.user.fname),('DIN Condensed', 40, 'bold'))

        desc = Label(self, text = 'You can create a group, join a group, or go solo for your budget management.\n',
                     font = ('Avenir Next Condensed',18))
        desc.grid(row=1, column = 0)

        curr_grps_frm = Frame(self)
        curr_grps_frm.grid(row = 2, column = 0, padx = 10, pady = 10)

        curr_grps_lbl = Label(curr_grps_frm, text = '\nYou are currently not a member of any groups.\n', font = ('Avenir Next Condensed', 15))
        curr_grps_lbl.pack()

        submit_b = Button(curr_grps_frm, text = 'Go', font = ('DIN Condensed', 12), width = 20)
        submit_b.pack()
        
        self.check_membership(curr_grps_lbl, submit_b)

        group_select_frm = Frame(self)
        group_select_frm.grid(row = 3, column = 0, padx = 10, pady = 10)

        create_group = Button(group_select_frm, text = 'Create a group...', font = ('DIN Condensed', 18), width = 20,
                          command = lambda: self.go_to(CreateGroup))
        create_group.pack()

        join_group = Button(group_select_frm, text = 'Join a group...', font = ('DIN Condensed', 18), width = 20,
                          command = lambda: self.go_to(JoinGroup))
        join_group.pack()

        self.check_all_grps(join_group)

        settings_b = Button(self, text = 'Settings', command = lambda: self.go_to(Settings))
        settings_b.grid(row = 4, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)
        
        log_out_b = Button(self, text = 'Log Out', command = self.log_out)
        log_out_b.grid(row = 5, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)

    def go_to(self, new_page):
        self.master.create_pages(new_page)
        self.master.go_to(new_page)

    def check_membership(self, label, button):
        if len(self.user.groups)==0:
            button['state']=DISABLED
        else:
            button['state']=NORMAL
            label['text'] = 'Your Groups:'
            label['font'] = ('DIN Condensed', 15)
        self.after(100, lambda: self.check_membership(label, button))

    def check_all_grps(self, button):
        pass
        """
        if len(GROUP_DATABASE)==0:
            button['state'] = DISABLED
        else:
            button['state'] = NORMAL
        self.after(100, lambda: self.check_all_grps(button))
        """

class Settings(GroupPage):
    def __init__ (self, master = None, window = None, **kwargs):
        GroupPage.__init__(self, master, window, **kwargs)

        self.create_title('Settings',('DIN Condensed', 40, 'bold'))

        self.name_reqs = [False, False, False] #Index 0: first name, Index 1: last name, Index 2: username
        self.char_req_pass = False
        self.num_req_pass = False

        curr_name_lbl = Label(self, text = 'Your name: {}'.format(GroupPage.curr_user.name), font = ('Avenir Next Condensed', 15))
        curr_name_lbl.grid(row = 1, column = 0)

        curr_uname_lbl = Label(self, text = 'Your username: {}'.format(GroupPage.curr_user.username), font = ('Avenir Next Condensed', 15))
        curr_uname_lbl.grid(row = 2, column = 0)

        change_uname_b = Button(self, text = 'Edit Username', command = self.show_uname_change)
        change_uname_b.grid(row = 3, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)

        delete_b = Button(self, text = 'Delete Account', command = self.delete)
        delete_b.grid(row = 4, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)
        
        cancel_b = Button(self, text = 'Cancel', command = self.log_out)
        cancel_b.grid(row = 5, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)

    def delete(self):
        response = messagebox.askyesno('Delete Account', 'Are you sure?\n(This action cannot be undone!)')
        if response == 1:
            conn = sql.connect('users.db')
            c = conn.cursor()
            c.execute("DELETE FROM users WHERE username = :uname",{'uname':GroupPage.curr_user.username})
            conn.commit()
            conn.close()
            messagebox.showinfo('Account Deleted!', 'This profile has been deleted.\n(Returning to home.)')
            self.log_out()

    def show_uname_change(self):
        change_window = Tk()
        change_window.title("Edit Username")

        change_frm = Frame(change_window, relief = FLAT)
        change_frm.pack()
        
        enter_lbl = Label(change_frm, text = 'Enter new username:', font = ('Avenir Next Condensed', 15))
        enter_lbl.grid(row = 0, column = 0)
        
        new_uname = Entry(change_frm)
        new_uname.grid(row = 0, column = 1)

        uname_check = Label(change_frm, text = 'Must be at least 5 characters.', font = ('Avenir Next Condensed', 12))
        uname_check.grid(row = 1, column = 1)
        
        submit_b = Button(change_window, text = 'Modify...', command = lambda:self.modify_uname(change_window, new_uname.get()))
        submit_b.pack()

        self.check_name_entry(new_uname, uname_check, 5, 2)
        self.check_name_modify_cond(submit_b, 2)

        cancel_b = Button(change_window, text = 'Cancel', command = lambda: self.close_window(change_window))
        cancel_b.pack()

    def close_window(self, window):
        window.destroy()

    def modify_uname(self, window, new_name):
        conn = sql.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = :uname", {'uname':new_name})
        all_records = c.fetchall()
        if new_name==GroupPage.curr_user.username:
            messagebox.showerror('Same Username',"""This is the same as your current username.\n
                                 Please input a different name, otherwise click the cancel button.""")
        elif len(all_records)>0:
            messagebox.showerror('Username already exists',"""Another user already has this username.\n
                                Please input a different name, otherwise click the cancel button.""")
        else:
            old_name = GroupPage.curr_user.username
            GroupPage.curr_user.username = new_name
            c.execute('UPDATE users SET username = :new_name WHERE username = :old_name', {'new_name': new_name, 'old_name': old_name})
            conn.commit()
            conn.close()
            messagebox.showinfo('Username reset', 'Your username has been successfully changed.')
            self.name_reqs[2] = False #Reset conditions for next username change
            change_window.destroy()

    def check_name_entry(self, entry, label, min_chars, req_index):
        if len(entry.get())>=min_chars:
            entry.config(highlightbackground = '#dbdbdb')
            label.grid_forget()
            self.name_reqs[req_index]=True
        else:
            entry.config(highlightbackground = 'green')
            entry.config(highlightthickness = 1)
            label.grid(row = entry.grid_info()['row']+1, column = 1, sticky = 'w')
            self.name_reqs[req_index] = False
        self.after(100, lambda:self.check_name_entry(entry,label,min_chars,req_index))

    def check_name_modify_cond(self, button, req_index):
        if self.name_reqs[req_index] == False:
            button['state'] = DISABLED
        else:
            button['state'] = NORMAL
        self.after(100, lambda:self.check_name_modify_cond(button, req_index))
        

class CreateGroup(GroupPage):
    def __init__ (self, master = None, window = None, **kwargs):
        GroupPage.__init__(self, master, window, **kwargs)
        
        self.input_frame = Frame(self)
        self.input_frame.grid(row = 1, column = 0, ipadx = 15, sticky = N)
        
        gname_lab = Label(self.input_frame, text = 'Enter Group Name', font = ('Avenir Next Condensed',15))
        gname_ent = Entry(self.input_frame, relief = FLAT)
        gname_lab.grid(row=0, column = 0, sticky = 'e')
        gname_ent.grid(row = 0, column = 1)

        num_members_lab = Label(self.input_frame, text = 'Enter Max Size', font = ('Avenir Next Condensed',15))
        num_members_ent = Entry(self.input_frame, relief = FLAT)
        num_members_lab.grid(row=1, column = 0, sticky = 'e')
        num_members_ent.grid(row = 1, column = 1)

        submit_b = Button(self, text = 'Submit', font = ('DIN Condensed', 12), width = 20)
        submit_b.grid(row = 3, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)

        cancel_b = Button(self, text = 'Cancel', command = self.log_out)
        cancel_b.grid(row = 4, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)


class JoinGroup(GroupPage):
    def __init__ (self, master = None, window = None, **kwargs):
        GroupPage.__init__(self, master, window, **kwargs)
            
        self.input_frame = Frame(self)
        self.input_frame.grid(row = 1, column = 0, ipadx = 15, sticky = N)

        submit_b = Button(self.input_frame, text = 'Go', font = ('DIN Condensed', 12), width = 20)
        submit_b.pack()
        
        cancel_b = Button(self, text = 'Cancel', command = self.log_out)
        cancel_b.grid(row = 4, column = 0, ipadx = 5, ipady = 5, padx = 30, pady = 30)


root = Tk()
root.title('Budget Database')
root.columnconfigure(0,weight = 1)
root.rowconfigure(0,weight = 1)
root.minsize(800,500)
App(root)
root.mainloop()
