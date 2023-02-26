from django.shortcuts import render
from django.http import HttpResponse


def form(request):


    return render(request, 'form.html', {})

def goal(request):

    if request.method != 'GET':
        return HttpResponse("El método POST no está soportado!")
    name = request.GET['name']
    return render(request, 'success.html', {'name':name})

def postForm(request):
    return render(request, 'postform.html', {})

def postGoal(request):
    if request.method != 'POST':
        return HttpResponse("El método GET no está soportado!")
    
    name = request.POST['name']
    return render(request, 'postsuccess.html', {'name':name})