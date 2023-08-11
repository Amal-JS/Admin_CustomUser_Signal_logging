#library used to get hashing algorithm
# Example: Using hashlib.sha256 
import hashlib
from django.db import models

# Create your models here.


class Custom_User(models.Model):

    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    img= models.ImageField(upload_to="user_profile_pic/" ,blank=True,null=True)
    phone_number= models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    is_super_user = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
    

    def make_password(self, raw_password):
        
        #hashing logic
        
        salt = 'abcdefghijk'  # Add a unique salt value

        hashed_password = hashlib.sha256((salt + raw_password).encode()).hexdigest()
        return hashed_password
    
#checking password when loging 
#the input password will be hashed and checked with the user object password hashed value

    def check_password(self, raw_password):
        hashed_input_password = self.make_password(raw_password)
        return self.password == hashed_input_password
    
    
