import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasking.settings')

import django

django.setup()

import random
from task1.models import *
from faker import Faker

fakegen = Faker()
topics = []


def add_topic():
    t = User.objects.get_or_create(username=random.choice(topics))[0]
    t.save()
    return t


def populate(N=20):
    for entry in range(N):
        top = add_topic()
        fake_pass = fakegen.password()
        fake_date = fakegen.join_date()
        fake_task_title = fakegen.task_title()
        fake_des = fakegen.task_title()
        fake_pic = fakegen.task_pic()
        fake_stamp = fakegen.create_time_stamp()
        fake_name = fakegen.company()
        task = Tasks.objects.get_or_create(name=user,  title=fake_task_title,des=fake_des,pic=fake_pic,stamp=fake_stamp )[0]
        user = User.objects.get_or_create(topic=top, url=fake_pass, date=fake_date, name=fake_name,)[0]

    if __name__ == '__main__':
        print("populating script!")
        populate(20)
        print("populating complete!")

