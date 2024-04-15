from django.db.models import F
from django.db.models import DEFERRED
from MainProject.models import *

def addToGroup(user,group) :
    try:
        groupeTest = Group.objects.filter(name = group).first()
        userTest = User.objects.filter(username = user).first()
        userTest.group = groupeTest
        userTest.save()
        return 1
    except :
        return 0
    

def removeFromGroup(user, group):
    try:
        groupeTest = Group.objects.filter(name = group).first()
        userTest = User.objects.filter(username = user,group = groupeTest).first()
        userTest.group = None
        userTest.save()
        return 1
    except :
        raise Exception("remove user in group failed")

def createGroup(name):
    try:
        groupe=Group(name=name)
        groupe.save()
        return 1
    except:
        return 0

def deleteGroup(name):
    try:
        groupe=Group.objects.filter(name=name)
        groupe.delete()
        return 1
    except:
        return 0
    
def getGroups():
    try:
        return Group.objects.all()
    except:
        return 0
    

def createUser(username):
    try:
        user=User(username = username)
        user.save()
        return 1
    
    except:
        return 0

def deleteUser(username):
    try:
        user=User.objects.filter(username=username)
        user.delete()
        return 1
    except:
        return 0
    
def getUser(username):
    try:
        return User.objects.filter(username=username).first()
    except:
        return 0

def getGroup(name):
    try:
        return Group.objects.filter(name=name).first()
    except :
        return 0

def getUsersFromGroup(name):
    try:
        idGrp = getGroup(name).id
        return list(User.objects.filter(group = idGrp))
    except:
        return 0
    

def getAllUsers():
    try:
        return User.objects.all()
    except:
        return 0