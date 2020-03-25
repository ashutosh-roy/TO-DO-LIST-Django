from django.db import models

# Create your models here.
class detail(models.Model):
    email= models.CharField(max_length=200)
    phone = models.IntegerField()
    country = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add = True)  

    #This function send the value to the template in which it has been called 
    #In this case it has returned "email"
    def __str__(self):
        return self.email
