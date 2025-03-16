from django.shortcuts import render

# Create your views here.
from  django . shortcuts  import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp import models
from myapp.models import Task
from django.contrib.auth.decorators import login_required
 


@login_required(login_url='/loginn')
def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/loginn')
    
    return render(request, 'index.html')
        

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/loginn')
    return render(request, 'loginn.html')
        
@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.Task(title=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.Task.objects.filter(user=user).order_by('-date')
        return redirect('/todopage',{'res':res})
        
    
    res=models.Task.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res,})

def deleteTask(request,srno):
    print(srno)
    obj=models.Task.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

@login_required(login_url='/loginn')
def editTask(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Task.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = models.Task.objects.get(srno=srno)
    return render(request, 'EditTask.html', {'obj': obj})





def signout(request):
    logout(request)
    return redirect('/loginn')

