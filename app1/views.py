from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from app1.serializers import UserSerializer
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from . import urls



def home(request):
     if request.method=="POST":
          name=request.POST['name']
          password=request.POST['password']
          email=request.POST['email']
          phone=request.POST['phone']
          details=Users(Name=name, Password=password, Email=email, Phone=phone)
          details.save()
          return redirect('signup/')
     url = signup
     print(url)
     print(reverse(url))
     return render(request, 'app1/home.html')
     # return JsonResponse({'message':'Inserted'})
  
def signup(request):
     info_details=Users.objects.all()
     return render(request, 'app1/signup.html',{'details':info_details})

def login(request):
     if request.method=="POST":
          email = request.POST['email']
          password = request.POST['password']

          try:
            current_user = Users.objects.get(Email=email, Password=password)
            request.session['user_id'] = current_user.id
            return redirect('profile')

          except Users.DoesNotExist:
            return render(request, 'app1/login.html', {'message': 'login failed'})
     return render(request, 'app1/login.html')

def logout(request):
    del request.session['user_id']
#     request.session.flush()
    return redirect('login')

def profile(request):
     print(request.session['user_id'])
     currentUser = request.session['user_id']
     userDetails=Users.objects.get(id=currentUser)
     print (userDetails)
     return render(request, 'app1/profile.html',{'details':userDetails})


def delete(request, id):
     Users.objects.get(id=id).delete()
     return redirect('signup')

def update(request,id):
     if request.method=="POST":
          name=request.POST['first']
          password=request.POST['second']
          email=request.POST['email']
          phone=request.POST['number']
          Users.objects.filter(id=id).update(Name=name, Password=password, Email=email, Phone=phone)
          return redirect('signup')
     else:
          userdata=Users.objects.get(id = id)
     return render(request,"app1/update.html", {"userdata": userdata})
     	
 
def upload(request):
     if request.method=='POST' and request.FILES['doc']:
          upload_file=request.FILES['doc']
          fs = FileSystemStorage()
          filename = fs.save(doc.name, doc)
          upload_file_url = fs.url(filename)
          return render(request, 'upload.html',{'uploaded_file_url': upload_file_url})
     
     return render(request, 'upload.html')

@csrf_exempt
def check_name_exist(request):
    name=request.POST.get("name")
    user_obj=Users.objects.filter(Name=name).exists()
    if user_obj:
        return HttpResponse(True)
    else:  
        return HttpResponse(False)

@csrf_exempt
@api_view(['GET', 'POST'])
def api_exFn(request, id=0):
     if request.method == 'POST':
          # user_data=JSONPars 
          pprint(user_data)
          user_serializer = UserSerializer(data=user_data)
          if user_serializer.is_valid():
               user_serializer.save()
               return JsonResponse('data inserted successfully',safe=False)
          return JsonResponse('insertion failed', safe=False)
     elif request.method=='GET':
          User=Users.objects.all()
          user_serializer=UserSerializer(User,many=True)
          return Response(user_serializer.data)
     elif request.method=='DELETE':
          print(id)
          User=Users.objects.get(id=id)
          User.delete()
          return JsonResponse({'message': 'data deleted successfully..'})
     elif request.method=='PUT':
          user_data=JSONParser().parse(request)
          print(user_data)
          User=Users.objects.get(id=user_data['id'])
          user_serializer = UserSerializer(User,user_data)
          if user_serializer.is_valid():
               user_serializer.save()
               return JsonResponse('data updated successfully',safe=False)
     return Response('updation failed')


def StuReg(request):
     if request.method=="POST":
          name=request.POST['name']
          password=request.POST['password']
          email=request.POST['email']
          phone=request.POST['phone']
          date=request.POST['date']
          details=student(stuName=name, stuPassword=password, stuEmail=email, stuPhone=phone, admnDate=date)
          details.upper()
          details.save()
          # return redirect('')
     return render(request, 'app1/stureg.html')

def studata(request):

     return render(request, 'app1/studata.html')

@api_view(['GET'])
def index(request):
     msg = "hello"
     return Response(msg)
     