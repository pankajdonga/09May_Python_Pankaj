from django.db import models

# Create your models here.

class usersignup(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    adhar=models.BigIntegerField()

    

