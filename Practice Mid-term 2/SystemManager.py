class SystemManager:
    '''A class for managing system operations.
    '''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def check_username_password(self, users, username, password):
        '''
        Checks whether the username exists in the users dictionary and that the password matches the username.  Returns boolean.
        '''
        
        if (username in users) and (users[username] == password):
            return True
        else:
            return False
    
    def is_valid_password(self, password):
        '''
        Checks whether the given password is valid.  Returns boolean.
        The length of a valid password should be at least 8 characters and it should contain
        at least one lowercase character, one uppercase character, and one number.
        '''
        
        if len(password) < 8:
            return False

        lowercase = False
        uppercase = False
        number = False

        for char in password:
            if char.islower() and not lowercase:
               lowercase = True

            elif char.isupper() and not uppercase:
                uppercase = True

            elif char.isdigit() and not number:
                number = True

        return (lowercase and uppercase and number)
    
    def sign_up(self, users, logged_in, username, password):
        '''
        Allows users to sign up.
        If the username already exists in the users dictionary, prints a friendly message.
        If the password does not satisfy the rule(s) (not valid), prints a friendly message.
        Otherwise, saves the username and the corresponding password in the users dictionary, and prints a
        success message.

        Note(s):
        The user is not automatically logged in when he/she signs up.
        '''

        # determine if sign up was correct
        success = False

        if username in users:
            print('Sorry, The username already exists.')

        elif not self.is_valid_password(password):
            print('The given password does not pass the requirements.')

        else:
            users[username] = password
            logged_in[username] = False
            print('Welcome, ' + username)
            success = True

        return success

    def log_in(self, users, logged_in, username, password):
        '''
        Allows users to log in.
        If the username does not exist in the users dictionary or the password is incorrect, prints an error message.
        Otherwise, saves the username and the value of True in the logged_in dictionary, and prints a welcome message.

        Note(s):
        Even if a user is already logged in, he/she can log in again.
        '''

        success = False

        if (self.check_username_password(users,username, password)):
            print('Welcome Back, ' + username)
            logged_in[username] = True
            success = True
        else:
            print('Invalid username or password')

        return  success

    
    def change_password(self, users, username, old_password, new_password):
        '''
        Allows users to change their password.
        If the username does not exist in the users dictionary, prints an error message.
        If the old_password is incorrect, prints an error message.
        If the new_password does not satisfy the rule(s) (not valid), prints an error message.
        Otherwise, changes the user's password in the users database, and prints a success message.
        '''

        success = False

        if not self.check_username_password(users,username,old_password):
            print('Invalid username or password')
        elif not (self.is_valid_password(new_password)):
            print('The given password does not pass the requirement.')
        else:
            users[username] = new_password
            success = True

        return  success
    
    def delete_account(self, users, logged_in, username, password):
        '''
        Allows users to delete their account.
        If the username does not exist in the users database, prints an error message.
        If the old_password is incorrect, prints an error message.
        Otherwise, deletes the user's account from the users dictionary, and prints a success message.

        Note(s):
        Also deletes the user's information in the logged_in dictionary.
        '''

        success = False

        if self.check_username_password(users,username,password):
            del users[username]
            if username in logged_in:
                del logged_in[username]
            print('Successfully deleted')

            success = True

        else:
            print('Invalid username or password')

        return success
    
    def get_sign_ups(self, users):
        '''
        Returns a list of users who are signed up (in the users dictionary).
        '''
        
        return self.key_list(users)


    def get_log_ins(self, logged_in):
        '''
        Returns a list of users who are logged in (in the logged_in dictionary).
        '''

        return  self.key_list(logged_in)


    def key_list(self, dict):
        """
        Returns a list of key for the given dict
        Args:
            dict:

        Returns:

        """
        return list(dict.keys())