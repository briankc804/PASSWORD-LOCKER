class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empt user list

    def __init__(self,user_name,pass_word):
      #dockstring removed for simplicity
      
         self.user_name = user_name
         self.pass_word = pass_word