from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def SignUp_View(request):
    if request.method=="POST":
        UserName=request.POST.get("username")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        ConfirmPassword=request.POST.get("confirmpassword")
        #print(UserName,Email,Password,ConfirmPassword)
        if Password != ConfirmPassword:
            return HttpResponse('Password is wrong ')
        try:
            if User.objects.get(username=UserName):
                return HttpResponse('UserName is Taken')
        except:
            pass
        
        myuser=User.objects.create_user(UserName,Email,Password)
        myuser.save()
        return HttpResponse('Sign Up Successfully done .. please continue with login.')
    return render(request,'SignUp.html')

def Login_View(request):
    return render(request,'Login.html')