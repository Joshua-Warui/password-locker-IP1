import unittest
from password_locker import User

class testUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''


  def setUp(self):
    '''
    setUp method to run before each test cases
    '''

    self.new_user = User("User1","TheFirst")


  def tearDown(self):
    '''
    tearDown method to clean up after each test case has run
    '''

    User.user_list = []

  
  def test_init(self):
    '''
    test_init case to test if object is initialized properly
    '''

    self.assertEqual(self.new_user.user_name,"User1")
    self.assertEqual(self.new_user.password,"TheFirst")


  def test_save_user(self):
    '''
    test_save_user case to test if object is saved to user_list list
    '''

    self.test_user = User("User2","The2")
    self.test_user.save_user()
    self.assertEqual(len(User.user_list),1)

  


  def test_save_multiple_user(self):
    '''
    test_save_multiple_user case to test if multiple user objects can be saved to user_list
    '''

    self.test_user = User("User2","The2")
    self.new_user.save_user()
    self.test_user.save_user()
    self.assertEqual(len(User.user_list),2)


  def test_delete_user(self):
    '''
    test_delete_user case to test if user can be deleted from user_list
    '''

    self.new_user.save_user()
    self.test_user = User("User2","The2")
    self.test_user.save_user()
    
    self.test_user.delete_user()
    self.assertEqual(len(User.user_list),1)





if __name__ == '__main__':
  unittest.main()

