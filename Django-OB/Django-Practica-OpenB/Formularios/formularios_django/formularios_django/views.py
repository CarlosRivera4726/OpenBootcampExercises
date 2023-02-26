from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm()
    return render(request, 'form.html', {'comment_form':comment_form})

def captura(request):
    if request.method != 'POST':
        return HttpResponse("Error de metodo")

    name = request.POST['name']

    return render(request, 'captura.html', {'name': name})

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form':form})

    elif request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Es válido!")
        else:
            return render(request, 'widget.html', {'form':form})