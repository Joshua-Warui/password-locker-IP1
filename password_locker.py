class User:
  '''
  Class that generates new instances
  '''

  user_list = []

  def __init__(self,user_name,password):
    '''
    __init method that helps us define properties for our objects

    Args:
      user_name: New user first name
      password: New user password
    '''

    self.user_name = user_name
    self.password = password


  def save_user(self):
    '''
    save_user method to save selected user to user_list list
    '''
  
    User.user_list.append(self)

  
  def delete_user(self):
    '''
    delete_user method to delete selected user from user_list
    '''

    User.user_list.remove(self)

