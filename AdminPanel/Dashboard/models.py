from django.db import models

# Create your models here.
class UserInfo(models.Model):
    photo=models.ImageField(upload_to='dashboard',blank=True)
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    Address=models.CharField(max_length=20)
    city=models.CharField(max_length=8)
    country=models.CharField(max_length=5)
    phoneNumber=models.BigIntegerField()
    companyName=models.CharField(max_length=15)
    postalcode=models.IntegerField(default=1234)

    def __str__(self):
        return self.username
    
class Login(models.Model):
    usrname=models.CharField(max_length=50)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.usrname

