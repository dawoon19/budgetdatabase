class Group:
    """A user-defined group of multiple users with budget constraints for
    specific purpose.
    """
    def __init__(self, name, initial_user = None):
        self.name = name
        self.users = []
        self.host = initial_user

    def add_user(self, user):
        self.users.append(user) 

GROUP_DATABASE = []

