from django.urls import path
from . import views


app_name = 'app-post'
urlpatterns = [
    path("", views.queries, name="index"),
    path("entries/<int:id>", views.entries, name="entries"),
    path("info/<int:idEntry>", views.info, name="info"),
    path("author/details/<int:id>", views.author, name="author/details"),
    path("update/", views.update, name="update"),
]
