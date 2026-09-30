from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  price=models.DecimalField(max_digits=10,decimal_places=2)
  description = models.TextField()
  supplier = models.CharField(max_length=200)
  product_image = models.ImageField(upload_to="products/")
  
  def __str__(self):
    return self.name
  
  
class User(models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  
  def __str__(self):
    return self.username
  
class Userprofile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  city = models.CharField(max_length=100)
  pincode = models.CharField(max_length=50)
  state = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  address = models.TextField()
  profile_pic = models.ImageField(upload_to="users/")
  
  def __str__(self):
    return f"{self.user.username} Profile"

