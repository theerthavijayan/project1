from django.shortcuts import redirect, render
from . models import Users

def home(request):
     if request.method=="POST":
          name=request.POST['name']
          password=request.POST['password']
          email=request.POST['email']
          phone=request.POST['phone']
          details=Users(Name=name, Password=password, Email=email, Phone=phone)
          details.save()
          return redirect('signup/')
     return render(request, 'app1/home.html')

def signup(request):
     info_details=Users.objects.all()
     return render(request, 'app1/signup.html',{'details':info_details})

def delete(request, id):
     Users.objects.get(id=id).delete()
     return redirect('signup')

