

import pyperclip

class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empt user list

    def __init__(self,user_name,pass_word):
      #dockstring removed for simplicity

         self.user_name = user_name
         self.pass_word = pass_word
         
         
        
         
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)  

    @classmethod
    def find_by_user_name(cls,user_name):
            '''
            Method that takes in a username and returns a user that matches that username.

            Args:
                username: name to search for
            Returns :
                user of person that matches the username.
            '''

            for user in cls.user_list:
                if user.user_name == user_name:
                    return user        


    @classmethod
    def user_exist(cls,user_name):
            '''
            Method that checks if a user exists from the user list.
            Args:
                user_name: user_name to search if it exists
            Returns :
                Boolean: True or false depending if the user exists
            '''
            for user in cls.user_list:
                if user.user_name == user_name:
                        return True

            return False               

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list  

    @classmethod
    def copy_pass_word(cls,user_name):
        user_found = User.find_by_user_name(user_name)
        pyperclip.copy(user_found.pass_word)          