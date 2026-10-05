from django.shortcuts import render,redirect
from django.http import HttpResponse
from userapp.models import User,Product,Userprofile

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
      request.session["user_id"] = user.id
      request.session["user_name"] = user.username
      return redirect("dashboard_link")
    else:
      return HttpResponse("Invalid credentials")
  else:
    return render(request,"userapp/login.html")
  
  
def dashboard(request):
  products = Product.objects.all()
  return render(request,"userapp/dashboard.html",{"products":products})

def profileUpdate(request):
  if request.method == "POST":
    city = request.POST.get("city")
    pincode = request.POST.get("pincode")
    state = request.POST.get("state")
    country = request.POST.get("country")
    address = request.POST.get("address")
    profile_pic = request.FILES.get("profile_pic")
    
    user_id = request.session.get("user_id")
    user = User.objects.get(id = user_id)
    
    Userprofile.objects.create(user=user,city = city,state=state,pincode = pincode,address=address,country=country,profile_pic=profile_pic)
    return redirect("dashboard_link")
  else:
    return render(request,"userapp/profile_update.html")
  
  
def profile(request):
  user_id = request.session.get("user_id")
  user  = Userprofile.objects.filter(id = user_id).first()
  return render(request,"userapp/profile.html",{"user":user})

def product_details(request,id):
  return render(request,"userapp/product_details.html")
       

