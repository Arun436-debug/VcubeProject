from django.db import models

# Create your models here.

class Admin(models.Model):
    AdmnNo = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    

class Attendence(models.Model):
    rollnum = models.IntegerField(null=True)
    date = models.DateField(null=True)
    attendence = models.CharField(max_length=20,null=True)
    mock = models.CharField(max_length=10,null=True)
    test = models.CharField(max_length=10,null=True)
    casestudy = models.CharField(max_length=10,null=True)

class Students(models.Model):
    stdno = models.IntegerField(primary_key=True)
    StdName = models.CharField(max_length=30)
    qualification = models.CharField(null=True,max_length=20)
    phno = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    DOJ = models.DateField(null=True)
    batch = models.CharField(null=True,max_length=20)
    image = models.ImageField(null=True,upload_to='images/',)

    def __str__(self):
        return self.StdName
    

class Stdinfo(Students):
    class Meta:
        proxy = True
        ordering = ['stdno']

