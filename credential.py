import pyperclip
class Credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,account_name,user_name,pass_word):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.pass_word = pass_word


        contact_list = [] # Empty contact list
        # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)


    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in an account name and returns a credential that matches that account name.

        Args:
            account_name: name of account to search for
        Returns :
            Crdential of person that matches the account name.
        '''

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential   

    @classmethod
    def credential_exist(cls,account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            accout_name:account name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                    return True

        return False 

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list  

    @classmethod
    def copy_account_name(cls,user_name):
        credential_found = Credential.find_by_account_name(user_name)
        pyperclip.copy(credential_found.account_name)   

       
         