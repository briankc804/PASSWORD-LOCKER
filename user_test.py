import unittest #importing the unittest module
from user import User #importing the user classs

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
        self.new_user = User("briankc","brian2022",) # create contact object


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
        test_user =User("tenda","tenda123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("tenda","tenda123") # new contact
        test_user.save_contact()

        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.user_list),1)

   
if __name__ == '__main__':
    unittest.main()
