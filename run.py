#!/usr/bin/env python3.9
from credential import Credential
from user import User


def create_user(uname,pword):
    '''
    Function to create a new user
    '''
    new_user = User(uname,pword)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()  

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user() 

def find_user(user_name):
    '''
    Function that finds a user by user name and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that user name and return a Boolean
    '''
    return User.user_exist(user_name)   

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new user, du - display user, fu -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cu':
                print("New User")
                print("-"*10)

                print ("user name ....")
                u_name = input()

                print("password ...")
                p_word = input()

                


                save_users(create_user(u_name,p_word)) # create and save new user.
                print ('\n')
                print(f"New User {u_name} {p_word} created")
                print ('\n')

        elif short_code == 'du':

                if display_users():
                        print("Here is a list of all your users")
                        print('\n')

                        for user in display_users():
                                print(f"{user.user_name} {user.pass_word}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

        elif short_code == 'fu':

                print("Enter the username you want to search for")

                search_user_name = input()
                if check_existing_users(search_user_name):
                        search_user = find_user(search_user_name)
                        print(f"{search_user.user_name} ")
                        print('-' * 20)

                        print(f"user_name.......{search_user.user_name}")
                        print(f"user_name.......{search_user.user_name}")
                else:
                        print("That user does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")
                    
if __name__ == '__main__':

    main()                           





def create_credential(aname,uname,pword):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(aname,uname,pword)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()  

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential() 

def find_credential(account_name):
    '''
    Function that finds a user by account and returns the credential
    '''
    return Credential.find_by_account_name(account_name)

def check_existing_credentials(account_name):
    '''
    Function that check if a credential exists with that user name and return a Boolean
    '''
    return Credential.credential_exist(account_name)   

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New Credential")
                print("-"*10)

                print ("account name ....")
                a_name = input()

                print ("user name ....")
                u_name = input()

                print("password ...")
                p_word = input()

                


                save_credentials(create_credential(a_name,u_name,p_word)) # create and save new credential.
                print ('\n')
                print(f"New Credential {a_name},{u_name} {p_word} created")
                print ('\n')

        elif short_code == 'dc':

                if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for credential in display_credentials():
                                print(f"{credential.account_name} {credential.user_name} {credential.pass_word}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any credentials saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the account name you want to search for")

                search_account_name = input()
                if check_existing_credentials(search_account_name):
                        search_credential = find_credential(search_account_name)
                        print(f"{search_credential.account_name} ")
                        print('-' * 20)

                        print(f"account_name.......{search_credential.account_name}")
                        print(f"account_name.......{search_credential.account_name}")
                else:
                        print("That credential does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")
                    
if __name__ == '__main__':

    main()                               