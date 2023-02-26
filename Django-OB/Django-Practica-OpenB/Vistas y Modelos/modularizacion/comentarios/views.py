from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.

def test(request):
    return HttpResponse("Funciona OK")


def create(request):
    comment1 = Comment(
        name="Sugerencia",
        score=5, 
        comment="Ten paciencia, todo se puede!"
    )

    comment1.save()

    return HttpResponse("Created!")


def delete(request):
    Comment.objects.filter(id=2).delete()
    return HttpResponse("deleted")