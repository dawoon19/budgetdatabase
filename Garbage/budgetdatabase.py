class Database:
    """ Collects all necessary data for all users.
    """
    users = []

class Category:
    """ Represents the category 
    """

class User:
    """ A user can input their budget and see how much money they have left.
    """
    name = ''
    budget = 0
    spent = 0
    profit = 0
    password = ''
    has_password = False
    unlocked = False

    def __init__(self, name, password=''):
        self.name = name
        if password != '':
            has_password = True
            self.password = password

    def unlock(self, pwatt=''):
        attempts = 0
        if self.has_password:
            if pwatt!=password:
                attempts+=1
                return 'Incorrect, attempts: '+ str(attempts)
            else:
                self.unlocked = True

    def is_unlocked(self):
        return unlocked

    def update_budget(self, amt):
        
        budget = amt
        
    def __str__(self):
        result = "User: " + self.name
        
        
