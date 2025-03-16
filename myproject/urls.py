
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup,name='signup'),
    path('loginn/', views.loginn,name='loginn'),
    path('todopage', views.todo,name='todopage'),
    path('deleteTask/<int:srno>', views.deleteTask,name='deleteTask'),
    path('editTask/<int:srno>', views.editTask, name='editTask'),
    path('signout/', views.signout, name='signout'),
]
