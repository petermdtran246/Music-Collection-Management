from users import User
class musicCollection:
    def __init__(self):
        self.current_user = None
        # A dictionary to store users
        self.users = {}

    # Adds a new user to the collection.
    def add_user(self, username):
        # Prints a message if the user was added successfully or already exists.
        if username in self.users:
            print(f'User {username} already exists.')
        else:
            self.users[username] = User(username)
            self.current_user = self.users[username]
            print(f'User {username} added and selected as the current user.')

    # Switches the current user to the user with the provided username.
    def change_user(self, username):
        # Prints a message if the user was switched successfully or not found.
        if username in self.users:
            self.current_user = self.users[username]
            print(f'User switched to {username}.')
        else:
            print(f'User {username} not found. Please add the user first.')

    # Returns the current user object, or None if no user is selected.
    def get_current_user(self):
        # Prints a message informing the user that no user is selected.
        if self.current_user:
            return self.current_user
        else:
            print('No user selected. Please add or change user.')
            return None






