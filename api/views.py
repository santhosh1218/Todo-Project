from django.shortcuts import render
from django.http import JsonResponse
from todoapp.models import Task
from api.serializer import Taskserializer,Userserializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK
# Create your views here.
## Function based Rest API's
@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def getemp(request):
    if request.method=='GET':
        pagination=PageNumberPagination()
        pagination.page_size=3
        data=Task.objects.all()
        paginated_task=pagination.paginate_queryset(data,request)
        task=Taskserializer(paginated_task,many=True)
        return pagination.get_paginated_response(task.data)
    if request.method=='POST':
        taskdata=Taskserializer(data=request.data)
        if taskdata.is_valid():
            taskdata.create_task()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])  
def modifytask(request,pk):
    taskdetail=Task.objects.get(id=pk)
    if request.method=='PUT':
        taskdata=Taskserializer(taskdetail,data=request.data)
        if taskdata.is_valid():
            taskdata.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        taskdata=Taskserializer(taskdetail)
        return Response(taskdata.data)
    else:
        taskdetail.delete()
        return Response(status=HTTP_200_OK)
    
@api_view(['POST'])
def registerapi(request):
    userdata=Userserializer(data=request.data)
    if userdata.is_valid():
        uobj=User.objects.create(username=userdata.validated_data['username'],email=userdata.validated_data['email'])
        uobj.set_password(userdata.validated_data['password'])
        uobj.save()
    else:
        return Response(status=HTTP_400_BAD_REQUEST)

## Class based API's
class Getpostapi(APIView):
   # authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    def get(self,request):
        task=Task.objects.all()
        taskdata=Taskserializer(task,many=True)
        return Response(taskdata.data)
    def post(self,request,**kwargs):
        taskdata=Taskserializer(data=request.data)
        if taskdata.is_valid():
            taskdata.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

class Putfetch(APIView):
    def get(self,request,pk=None):
        task=Task.objects.get(id=pk)
        taskdata=Taskserializer(task)
        return Response(taskdata.data)
    

# CLASS BASED GENERIC VIEWS
class Genericapiview(ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=Taskserializer
    pagination_class=PageNumberPagination
