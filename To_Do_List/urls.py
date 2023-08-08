"""
URL configuration for To_Do_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todos.views import todo_list_view, TodoCreate ,TodoUpdateAPIView
from users.views import register_user, user_login
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list_view, name='todo-home' ),
    path('create/', TodoCreate, name='todo-create'),
    path('update/<int:id>', TodoUpdateAPIView.as_view(), name= 'todo-update'),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('doc/', include(swagger)),
]
