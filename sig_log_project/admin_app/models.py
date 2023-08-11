from django.db import models


# Create your models here.


class LogUser(models.Model):
    
    #specify activity either account created or account updated
    activity = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    phone_number= models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    
   
    


    def __str__(self):
        return f"{self.username} {self.activity} on {self.time}"
