
from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('', views.index, name="index"),
    path('<letter>', views.index, name="index"),
    path('view/<int:id>', views.view, name="view"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('register/', views.register, name="register")
]