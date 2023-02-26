from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/form/', views.form, name="form"),
    path('get/goal/', views.goal, name="goal"),
    path('post/form/', views.postForm, name="postForm"),
    path('post/goal/', views.postGoal, name="postGoal"),
]
