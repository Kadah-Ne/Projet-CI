from django.db import models

# Create your models here.

class User(models.Model) :
    id = models.AutoField(primary_key=True,null=False)
    username = models.CharField(max_length = 255, null = False)
    group = models.ForeignKey('Group',on_delete = models.CASCADE,null = True)
    isAdmin = models.BooleanField(default = False)

class Group(models.Model) :
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length = 255, null = False)