from django.forms import ModelForm
from .models import User,Tasks
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password','join_date')


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('uid','task_title','task_description','task_pic','create_time_stamp')