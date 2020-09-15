from django.shortcuts import render
from django.contrib.auth import authenticate, login


#Create your views here.

def login_view(request):
     if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         user = authenticate(username=username, password=password)
         if user is not None:
             print("인증 성공")
             login(request, user)
         else:
             print("인증 실패")

     return render(request, "users/login.html")

def signup_view(request):
    
    return render(request, "users/signup.html")

def introduce_view(request):
    
    return render(request, "users/introduce.html")

def policy_view(request):
    
    return render(request, "users/policy.html")