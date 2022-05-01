from django.db import models
from sqlalchemy import null

# Create your models here.
class Infomatsion(models.Model):
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phonenumer = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,default='photos/default.jpg')
    
    
    mehnat = models.IntegerField(default=0)
    faoliyat = models.IntegerField(default=0)
    project = models.IntegerField(default=0)
    mukofot = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.frist_name + ' ' + self.last_name
    
    def fullname(self):
        return self.frist_name + ' ' + self.last_name
    
    
class Service(models.Model):
    images = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    def __str__(self):
        return self.title
    