from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from authapp.models import *
# Create your views here.
def SignUp_View(request):
    if request.method=="POST":
        UserName=request.POST.get("username")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        ConfirmPassword=request.POST.get("confirmpassword")
        #print(UserName,Email,Password,ConfirmPassword)
        if Password != ConfirmPassword:
           messages.warning(request,'Password is incorrect')
           return redirect('/signup')
        try:
            if User.objects.get(username=UserName):
                messages.warning(request,'UserName is Already Taken')
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=Email):
                messages.warning(request,'Email is Already Taken')
                return redirect('/signup')
        except:
            pass

        myuser=User.objects.create_user(UserName,Email,Password)
        myuser.save()
        messages.success(request,'Suceessfully completed your registration..Please Login!')
        return redirect('/login')
    return render(request,'SignUp.html')

def Login_View(request):
    if request.method=="POST":
        UserName=request.POST.get("username")
        Password=request.POST.get("password")
        myuser=authenticate(username=UserName,password=Password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Success')
            return redirect('/home')
        else:
            messages.error(request,'Invalid Credentials..')
            return redirect('/login')

    return render(request,'Login.html')


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphonenumber=request.POST.get("num")
        fdescription=request.POST.get("Description")

        print(fname,femail,fphonenumber,fdescription)
        messages.info(request,f'The name is {fname},email is {femail},Phonenumber is{fphonenumber}&your query is{fdescription}')

        query=Contacts(name=fname,email=femail,phonenumber=fphonenumber,description=fdescription)
        query.save()
        messages.success(request,"Thanks For Contating us")
    return render(request,'contact.html')