from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onetoone/', include('onetoone.urls', namespace='onetoone'), name="onetoone"),
    path('manytoone/', include('manytoone.urls', namespace='manytoone'), name="manytoone"),
    path('manytomany/', include('manytomany.urls', namespace='manytomany'), name="manytomany"),
]
