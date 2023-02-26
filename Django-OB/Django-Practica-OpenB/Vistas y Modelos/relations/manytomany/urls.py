from django.urls import path, include
from . import views


app_name = "manytomany"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create")  
]
