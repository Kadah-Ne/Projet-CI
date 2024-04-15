from django.db.models import F
from django.db.models import DEFERRED
from MainProject.models import *

def addToGroup(user,group) :
    return 0

def removeFromGroup(user, group):
    return 0

def createGroup(name):
    try:
        groupe=Group(name)
        groupe.save()
        return 1
    
    except:
        raise Exception("insert group failed")

def deleteGroup(name):
    return 0

def getUser(username):
    return None

def getUsersFromGroup(name):
    return [None, None, None]

def getAllUsers():
    return [None, None, None]

def createUser(username):
    try:
        user=User(DEFERRED, username, 0, False)
        user.save()
        return 1
    
    except:
        raise Exception("insert user failed")

def deleteUser(username):
    return 0