from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', include('contact.urls', namespace="contact"), name="contact"),
    path('todo/', include('todo.urls', namespace="todo"), name="todo")
]
