from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UserForm,TaskForm

def createUserView(response):
    registered = False
    if response.method == 'POST':
        form = UserForm(response.POST)

        if form.is_valid():
            user = form.save()
            #user.set_password(user.password)
            user.save()
            return render(response, 'createtask.html')
        else:
            print(UserForm.errors)
        registered = True

    else:
        form = UserForm()
    return render(response, 'signin.html', {'form': form, 'registered':registered})


@login_required()
def special(request):
    login(request)
    return HttpResponse("You are logged in, Nice!")


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')

            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")

        else:
            print("Someone tried to Login and Failed!")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    return render(request,'login.html')

def CreateTask(request):
    #uid = User.objects.get(uid =uid)
    if request.method == 'POST':
        #taskform = TaskForm(response.POST)
        taskform = TaskForm(request.POST, request.FILES)

        if taskform.is_valid():
            task = taskform.save()

            if 'task_pic' in request.FILES:
                task.task_pic = request.FILES['task_image']
            task.save()

            return render(request, 'taskdisplay.html')

    else:
        taskform = TaskForm()
    return render(request, 'createtask.html', {'taskform': taskform})

def Displaytask(request):
    if request.method == 'GET':
        display = Tasks.objects.all()
    return render(request, "displaytask.html", {'display':display})