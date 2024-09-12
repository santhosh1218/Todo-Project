from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from todoapp.forms import UserRegistrationForm,TaskForm
from django.contrib.auth import login,logout,authenticate
from todoapp.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.
def Home(request):
    return render(request,'todoapp/home.html')
@login_required
def index(request):
    task=Task.objects.filter(user=request.user)x`x```
    return render(request,'todoapp/index.html',{'task':task})
@login_required 
def create_task(request):
    task=TaskForm()
    if request.method=='POST':
        task=TaskForm(request.POST)
        if task.is_valid():
            task.instance.user=request.user
            task.save()  
            return redirect('home')
        else:
            print(task.errors)
            return render(request,'todoapp/create.html',{'task':task})
    return render(request,'todoapp/create.html',{'task':task})
def complete_task(request):
    task=Task.objects.filter(user=request.user)
    return render(request,'todoapp/complete_task.html',{'task':task})
@login_required
def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('todoapp:index')
@login_required
def update_task(request,id):
    t=Task.objects.get(id=id)
    task=TaskForm(instance=t)
    if request.method=='POST':
        task=TaskForm(request.POST,instance=t)
        if task.is_valid():
            task.save()
            return redirect('todoapp:index')
    return render(request,'todoapp/update.html',{'task':task})

def filter_task(request):
    if request.method=='GET':
        return render(request,'todoapp/filter.html')
    else:
        task=request.POST.get('taskid')
        t=get_object_or_404(Task,id=task)
        if not t:
            raise ValidationError('enter valid id')
        elif t.user!=request.user:
            raise ValidationError('you are not authorised')
        return render(request,'todoapp/filter.html',{'task':t})
       
        

def Signup(request):
    form=UserRegistrationForm()
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'registration/signup.html',{'form':form})
    return render(request,'registration/signup.html',{'form':form})

def Login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=uname,password=password)
        if user!= None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'registration/login.html')
@login_required
def Logout(request):
    logout(request)
    return redirect('login')

