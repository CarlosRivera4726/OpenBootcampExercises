from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

#* página principal

def index(request, letter=None):

    if letter != None: contacts = Contact.objects.filter(first_name__istartswith=letter)
    
    else: contacts = Contact.objects.filter(first_name__contains=request.GET.get('search', ''))

    count = contacts.count()

    context = {
        'contacts': contacts,
        'count': count
    }
    return render(request, 'contact/index.html', context)

#* detalles de los contactos registrados

def view(request, id):
    try:
        contact = Contact.objects.get(id=id)
        context = {
            'contact': contact
        }
        return render(request, 'contact/detail.html', context)
    except:
        return redirect('/contact/')

#* editar contactos registrados

def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
        contactForm = ContactForm(instance=contact)
        context = {
            'contactForm': contactForm,
            'id':id
        }
        return render(request, 'contact/edit.html', context)

    if request.method == 'POST':
        contactForm = ContactForm(request.POST, instance=contact)
        
        if contactForm.is_valid():
            contactForm.save()
            context = {
            'contactForm': contactForm,
            'id':id
        }

        messages.success(request, 'Contacto Actualizado')
        return render(request, 'contact/edit.html', context)

#* Eliminar 1 contacto

def delete(request, id):
    try:
        contact = Contact.objects.get(id=id)
        contact.delete()
        messages.error(request, 'Contacto Eliminado')
    except:
        messages.info(request, 'No se encuentra el contacto!')
    finally:
        return redirect('/contact/')

#* registrar contactos
def register(request):
    contactForm = ContactForm()
    context = {
        'contactForm': contactForm
    }

    if request.method == 'GET':
        return render(request, 'contact/register.html', context)
        
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            messages.success(request, 'Contacto Registrado')
            return redirect('/contact/')
        else:
            return render(request, 'contact/register.html', context)
            