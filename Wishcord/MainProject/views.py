from django.shortcuts import render,redirect

from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def login(request):
    pass

def groupList(request):
    pass

def groupView(request):
    pass

def groupManage(request):
    pass

def adminPage(request):
    pass
