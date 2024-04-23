from django.shortcuts import render,redirect,reverse
import MainProject.dbFunctions as dbf
from django.http import HttpResponse
import random as rand

minUsers = 3

def maxUsers():
    nbGroups = dbf.getGroups().count()
    nbUsers = dbf.getAllUsers().count()
    print(nbUsers,nbGroups)
    if nbGroups > 0 and nbUsers >0:
        nbUserPerGroup = nbUsers//nbGroups
        if nbUsers%nbGroups < 2 :
            return nbUserPerGroup +1 
        else :
            return nbUserPerGroup

def index(request):
    dbf.clear()
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        query = request.POST
        if dbf.getUser(query["username"]):
            request.session["user"] = query['username']
            return redirect(groupList)
    return render(request,"login.html")
    pass

def createAccount(request):
    if request.method == 'POST':
        query = request.POST
        print(query)
        dbf.createUser(query['username'])
        request.session["user"] = query['username']
        maxUsers()
        return redirect(groupList)
    return render(request,"createAccount.html")
    

def groupList(request):
    if "user" in request.session:
        if request.method=="POST":
            query = request.POST
            print(query)
            if "name" in query:
                request.session["tmp_data"] = query['name']
                return redirect(groupManage)
            elif "creation" in query :
                return redirect(groupCreate)
            elif dbf.getGroups().count() > 1 :
                listGroups = dbf.getGroups()
                dbf.addToGroup(request.session["user"],rand.choice(listGroups).name)
        groups = dbf.getGroups()
        usersNoGrp = dbf.getGrouplesUsers()
        dicoGroupes = {}
        listeUser = []
        for i in groups:
            dicoGroupes[i.name] = dbf.getCountUsersFromGroup(i.name)
        for user in usersNoGrp:
            listeUser.append(user.username)
        print(listeUser)
        return render(request,"listGroups.html",{"groups" : dicoGroupes,"listUser":listeUser})
    else :
        return redirect(login)

def groupManage(request):
    if request.session["tmp_data"]:
        listUsers = dbf.getUsersFromGroup(request.session["tmp_data"])
        if request.method == "POST":
            query = request.POST
            if "user" in query:
                print(query['user'],request.session["tmp_data"])
                dbf.removeFromGroup(query['user'],request.session["tmp_data"])
                if dbf.getCountUsersFromGroup(request.session["tmp_data"]) < 2 :
                    dbf.deleteGroup(request.session["tmp_data"])
                    return redirect(groupList)
            elif not dbf.isUserInGroup(request.session["user"],request.session["tmp_data"]):
                if dbf.getCountUsersFromGroup(request.session["tmp_data"]) < maxUsers() :
                    dbf.addToGroup(request.session["user"],request.session["tmp_data"])
            return redirect(reverse(groupManage))
    return render(request,"groupManage.html",{'groupUsers':listUsers})
    
def groupCreate(request):
    if request.method == "POST":
        query = request.POST
        if "newGuys" in query :
            if (maxUsers() == None or maxUsers()>minUsers) and (query['grpName'] != "" and query['grpName'] != None):
                print("a")
                dbf.createGroup(query['grpName'])
                dbf.addToGroup(request.session["user"],query["grpName"])
                dbf.addToGroup(query["newGuys"],query["grpName"])
                return redirect(groupList)
    listUsers = dbf.getGrouplesUsers()
    listeUser2 = []
    for i in listUsers:
        if i.username != request.session["user"]:
            listeUser2.append(i)
            
    return render(request,"groupCreate.html",{"users" : listeUser2})

def adminPage(request):
    allUsers = dbf.getAllUsers()
    allGroups = dbf.getGroups()
    NbUsers = allUsers.count()
    NbGroups = allGroups.count()
    listUsers = []
    listGroups = []
    maxU=0
    for user in allUsers:
        listUsers.append(user.username)
    for group in allGroups:
        count = dbf.getCountUsersFromGroup(group.name)
        listGroups.append((group.name,count))
        maxU = max(maxU,count)
    return render(request,"adminPage.html",{"NbUsers":NbUsers,"listUsers" : listUsers,"NbGroups":NbGroups,"listGroups" : listGroups,"max":maxU})
    
