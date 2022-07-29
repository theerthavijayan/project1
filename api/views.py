from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *

# @api_view(['POST'])
# def api_insert(request):
#     return Response('working')

@api_view(['POST'])
def api_insert(request):
    ins_data = request.data     #data that we get from frontend stored to variable ins_data
    obj = ApiCrud(name=ins_data['name'],address=ins_data['address'],contact=ins_data['contact'],gender=ins_data['gender'],email=ins_data['email'] )   # in bracket model name = variable above['key passed']
    obj.save()
    return Response('successfull!')

@api_view(['GET'])
def api_show(request):
    queryset = ApiCrud.objects.all()
    data = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender,'email':blog.email} for blog in queryset]
    return Response({'data':data})
    
@api_view(['DELETE'])
def delete(request,id):
    ApiCrud.objects.get(id = id).delete()
    return Response('deleted')

@api_view(['PUT'])
def view(request,id):
    blog = ApiCrud.objects.get(id = id)
    print(blog)
    data = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender,'email':blog.email}]
    return Response({'user':data})


@api_view(['GET'])
def addnum(request):
    n1 = request.GET.get('n1')
    n2 = request.GET.get('n2')

    print(n1)
    total =  int(n1)+int(n2)
    return Response(total)


