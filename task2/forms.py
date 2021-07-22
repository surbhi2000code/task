from django.forms import ModelForm
from .models import TaskTwo
from django import forms

class TaskForm(forms.ModelForm):
    class Meta():
        model = TaskTwo
        fields = ('title','parentID')

class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
