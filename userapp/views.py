from django.shortcuts import render,redirect
from django.http import HttpResponse
from userapp.models import User,Product

def signup(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    
    User.objects.create(username=username,email=email,phone=phone,password=password)
    
    return redirect("login_link")
  else:
    return render(request,"userapp/signup.html")
  
  
def login(request):
  if request.method=="POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    user = User.objects.filter(email = email,password=password).first()
    if(user):
      return redirect("dashboard_link")
    else:
      return HttpResponse("Invalid credentials")
  else:
    return render(request,"userapp/login.html")
  
  
def dashboard(request):
  products = Product.objects.all()
  return render(request,"userapp/dashboard.html",{"products":products})
      

