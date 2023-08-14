In this project we are going to :
    1. Create a model for users 
    2. We are going to use the built in User model for admin
    3. We are using Django Signals 
    4. We are gonna log all user activities with the help of signals for that we will create another model UserLog.
    

2.When you are using a custom user model and we want to use the built in authentication system with it then that model want to have these 
  fields

        1.last_login
        2.is_superuser
        3.is_active
        4.get_username() ...etc