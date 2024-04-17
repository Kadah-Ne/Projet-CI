from django.shortcuts import render,redirect,reverse
import MainProject.dbFunctions as dbf
from django.http import HttpResponse

def index(request):
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
        return redirect(groupList)
    return render(request,"createAccount.html")
    pass

def groupList(request):
    if request.method=="POST":
        query = request.POST
        print(query)
        if "name" in query:
            request.session["tmp_data"] = query['name']
            return redirect(groupManage)
        elif "creation" in query :
            return redirect(groupCreate)
    # dbf.testGroupes()
    groups = dbf.getGroups()
    dicoGroupes = {}
    for i in groups:
        dicoGroupes[i.name] = dbf.getCountUsersFromGroup(i.name)
    return render(request,"listGroups.html",{"groups" : dicoGroupes})

def groupManage(request):
    if request.session["tmp_data"]:
        listUsers = dbf.getUsersFromGroup(request.session["tmp_data"])
        if request.method == "POST":
            query = request.POST
            # user = dbf.getUser(query['user'])
            
            dbf.removeFromGroup(query['user'],request.session["tmp_data"])
            return redirect(reverse(groupManage))
    return render(request,"groupManage.html",{'groupUsers':listUsers})
    
def groupCreate(request):
    if request.method == "POST":
        query = request.POST
        dbf.createGroup(query['grpName'])
        dbf.addToGroup(request.session["user"],query["grpName"])
        return redirect(groupList)
    return render(request,"groupCreate.html")
def adminPage(request):
    pass
