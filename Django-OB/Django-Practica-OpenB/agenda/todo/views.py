from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def index(request):

  todos = Todo.objects.filter(title__contains=request.GET.get('search', ''))
  count = todos.count()

  context = {
        'todos': todos,
        'count': count
    }
  return render(request, 'todo/index.html', context)

def view(request, id):
  try:
    todo = Todo.objects.get(id=id)
    context = {
      'todo': todo
    }
    return render(request, 'todo/detail.html', context)
  except:
    messages.error(request, 'No se encontro la tarea con el id proporcionado')
    return redirect('/todo/')
  
def edit(request, id):
  try:
    todo = Todo.objects.get(id=id)
    
    if request.method == 'GET':
      
      todoForm = TodoForm(instance=todo)
      context = {
        'todoForm': todoForm,
        'id':id
      }
      return render(request, 'todo/edit.html', context)
      
    if request.method == 'POST':
      
      todoForm = TodoForm(request.POST, instance=todo)
      if todoForm.is_valid():
        context = {
          'todoForm': todoForm,
          'id':id
        }
        todoForm.save()
        messages.success(request, 'La tarea se ha modificado exitosamente!')
        return redirect(f'/todo/edit/{id}')

  except:
    messages.error(request, 'No se encontro la tarea con el id proporcionado')
    return redirect('/todo/')

def delete(request, id):
  try:
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.success(request, 'Se ha eliminado la tarea con el id proporcionado')
    return redirect('/todo/')
  except:
    messages.error(request, 'No se encontro la tarea con el id proporcionado')
    return redirect('/todo/')

def register(request):
  if request.method == 'GET':
    todoForm = TodoForm()
    context = {
      'todoForm': todoForm
    }
    return render(request, 'todo/register.html', context)
  
  
  if request.method == 'POST':
    todoForm = TodoForm(request.POST)
    context = {
        'todoForm': todoForm
    }
    if todoForm.is_valid():
      todoForm.save()
      return redirect('/todo/')
    else:
      return render(request, 'todo/register.html', context)