class SystemCreator:
    '''A class for loading user credential information from a file, storing it
    in a dictionary, and creating a second dictionary that keeps track of which
    users are currently logged in.'''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def init_db(self, file):
        '''
        Loads the given .csv file containing user credentials.
        Each row is a comma-separated list including username and password.

        Example(s):
        lbrandon,My_Crazy_Password_1234
        tjones,4er3yw6rt5R
        dennisq,0987poiu1234QwEr

        Stores the usernames and passwords in a users dictionary where the
        username is the key and the password is the value.

        Creates an empty logged_in dictionary for storing user log-ins where the
        username is the key and the value is a bool indicating
        if the user is logged in or not.
        '''
        users = {}

        f = open(file,'r')
        for line in f:
            line = line.strip()
            user_info = line.split(',')
            username = user_info[0].strip()
            password = user_info[1].strip()
            users[username] = password
        f.close()

        """
        while open(file,'r') as f:
            for line in f:
                line = line.strip()
                user_info = line.split(',')
                username = user_info.strip()
                password = user_info[1].strip()
                users[username] = password
        """

        logged_in = {}

        # minor change
        
        return users, logged_in