import unittest #importing the unittest module
from user import User #importing the user classs
import pyperclip
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("briankc","brian2022") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"briankc")
        self.assertEqual(self.new_user.pass_word,"brian2022")
        

    def test_save_user(self):
        '''
        test_save_user test case to test if the user user is saved into the user list
        '''  
        self.new_user.save_user() #saving the user
        self.assertEqual(len(User.user_list),1)  

    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Collins","Collins20") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Collins","Collins20") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)   

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our user list
        '''
        self.new_user.save_user()
        test_user = User("Collins","Collins20") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Collins","Collins20") # new user
        test_user.save_user()

        found_user = User.find_by_user_name("Collins")

        self.assertEqual(found_user.user_name,test_user.user_name)   


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Collins","Collins20") # new user
        test_user.save_user()

        user_exists = User.user_exist("Collins")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_users(),User.user_list)


    def test_copy_pass_word(self):
        '''
        Test to confirm that we are copying the password address from a found user
        '''

        self.new_user.save_user()
        User.copy_pass_word("briankc")

        self.assertEqual(self.new_user.pass_word,pyperclip.paste())
    
    
   
if __name__ == '__main__':
    unittest.main()
