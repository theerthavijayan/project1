from tokenize import Name
from django.shortcuts import render
from django.http import JsonResponse
from ajax.models import AjaxCrud
from django.views.decorators.csrf import csrf_exempt

def reg_page(request):
    return render(request, 'register.html')


@csrf_exempt
def register(request):
    uname=request.POST['name']
    password=request.POST['password']
    email=request.POST['email']
    phone=request.POST['phone']
    ajdet=AjaxCrud(Name=uname, Password=password,Email=email,Phone=phone)
    ajdet.save()
    return JsonResponse({'message':'Data Inserted'})


def display(request):
    return render(request, 'display.html')


def displaydata(request):
    disdata = AjaxCrud.objects.all()
    data=[{'id':x.id, 'name':x.Name, 'password':x.Password, 'email':x.Email, 'phone':x.Phone}for x in disdata]
    return JsonResponse({'data':data})

@csrf_exempt
def deletedata(request):
	id = request.POST['key_id']
	AjaxCrud.objects.get(id=id).delete()
	return JsonResponse({'message':'Data Deleted'})

@csrf_exempt
def updatedata(request):
    id = request.POST['id']
    print(id)
    updata = AjaxCrud.objects.get(id = id)
    updata1 = [{'id':updata.id, 'name':updata.Name, 'password':updata.Password, 'email':updata.Email, 'phone':updata.Phone}]
    print(updata1)
    return JsonResponse({'update':updata1})

@csrf_exempt
def update(request):
    id = request.POST['pkid']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    AjaxCrud.objects.filter(id = id).update(Name=name, Password=password,Email=email,Phone=phone)
    print(name)
    return JsonResponse({'message':'Data updated'})