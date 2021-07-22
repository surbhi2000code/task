from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'task1'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('task1.urls'))
    path('user/',views.createUserView),
    path('createtask/', views.CreateTask,name='createtask'),
    path('taskdisplay/', views.Displaytask, name = "displaytask")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


