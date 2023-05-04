from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def loginPage(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        username = User.objects.get(email=email).username
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None :
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
                
    context = {}
    return render(request,'authenticate/login.html',context)


@login_required(login_url='login')
def homePage(request):
    return render(request,'authenticate/home.html')

@login_required(login_url='login')
def userPage(request):
    return render(request,'authenticate/user.html')


def logoutUser(request):
    logout(request)
    return redirect('login')