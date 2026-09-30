from django.shortcuts import render,redirect
from userapp.models import User

def signup(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    
    User.objects.create(username=username,email=email,phone=phone,password=password)
    
    return redirect("signup_link")
  else:
    return render(request,"userapp/signup.html")

