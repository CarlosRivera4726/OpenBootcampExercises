from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.

def index(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'index.html', {'form': form})

    if request.method == 'POST':
        #guardar la informacion
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            form = ProductForm()
            return render(request, 'index.html', {'form': form}) 
        else:
            return render(request, 'index.html', {'form': form}) 
