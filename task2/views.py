from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def Task(request):
    if request.method == 'GET':
        display = TaskTwo.objects.all()
    return render(request, "task.html", {'display':display})
