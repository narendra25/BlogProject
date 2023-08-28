from django.shortcuts import render

# Create your views here.
def SignUp_View(request):
    return render(request,'SignUp.html')

def Login_View(request):
    return render(request,'Login.html')