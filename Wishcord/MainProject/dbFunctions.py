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
        
        for i in getUsersFromGroup(name) :
            i.group = None
            i.save()
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
    
def getCountUsersFromGroup(name) :
    try:
        idGrp = getGroup(name).id
        return list(User.objects.filter(group = idGrp)).__len__()
    except:
        return 0

def getAllUsers():
    try:
        return User.objects.all()
    except:
        return 0

def getGrouplesUsers():
    try:
        return User.objects.filter(group = None)
    except:
        return 0
    
def isUserInGroup(user,group):
    try:
        flag = False
        listUsers = getUsersFromGroup(group)
        for i in listUsers :
            if i.username == user:
                flag = True
        return flag
    except:
        return 0
    
def clear():
    for i in Group.objects.all() :
        i.delete()
    for i in User.objects.all():
        i.delete()

def testGroupes() :
    clear()
    createGroup("Premier Groupe")
    createUser("Martin")
    createUser("Oscar")
    createUser("Frank")
    addToGroup("Martin","Premier Groupe")
    addToGroup("Oscar","Premier Groupe")
    addToGroup("Frank","Premier Groupe")
    createGroup("2eme Groupe")
    createUser("Tom")
    createUser("François")
    
    addToGroup("Tom","2eme Groupe")
    addToGroup("François","2eme Groupe")
    