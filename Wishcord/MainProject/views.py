from django.shortcuts import render,redirect
import MainProject.dbFunctions as dbf
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request,"login.html")
    pass

def createAccount(request):
    return render(request,"createAccount.html")
    pass

def groupList(request):
    if request.method=="POST":
        
        query = request.POST
        print(query)
        return redirect(login)
    dbf.testGroupes()
    groups = dbf.getGroups()
    dicoGroupes = {}
    for i in groups:
        dicoGroupes[i.name] = dbf.getCountUsersFromGroup(i.name)
    return render(request,"listGroups.html",{"groups" : dicoGroupes})

def groupView(request):
    pass

def groupManage(request):
    pass

def adminPage(request):
    pass
