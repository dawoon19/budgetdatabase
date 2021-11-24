import sqlite3 as sql

class User:
    def __init__(self, fname, lname, uname, password):
        self.fname = fname
        self.lname = lname
        self.username = uname
        self.password = password
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    @property
    def name(self):
        return self.fname + ' ' + self.lname

    def __repr__(self):
        return "{} (Username: {})".format(self.name, self.username)

USER_DATABASE = []

def update_USER_DATABASE():
    conn = sql.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE users (
                    fname text,
                    lname text,
                    username text,
                    password text
                    )""")
    except sql.OperationalError:
        pass
    c.execute("SELECT * FROM users")
    all_users = c.fetchall()
    conn.commit()
    conn.close()
    if len(all_users)!=0:
        for user in all_users:
            USER_DATABASE.append(User(user[0], user[1], user[2], user[3]))

update_USER_DATABASE()
