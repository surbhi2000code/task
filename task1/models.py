from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True,max_length=200,default="")
    join_date = models.DateTimeField()
    password = models.CharField(max_length=10,default="")

    def __str__(self):
        return self.username

class Tasks(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    tid = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=200,default="")
    task_description = models.TextField(max_length=2000, null=True, default="")
    task_pic = models.ImageField(upload_to='media/task_image')
    create_time_stamp = models.DateTimeField()

    def __str__(self):
        return self.task_title