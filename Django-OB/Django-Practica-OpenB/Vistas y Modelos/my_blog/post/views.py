from django.shortcuts import render
from .models import Author, Entry

# Create your views here.

def index(request):
    return render(request, "post/index.html", {})

def queries(request):
    # modelo de author
    #* Obtenemos todos los elementos de la BD
    authors = Author.objects.all()

    '''
    #* Obtenemos datos filtrados por condición
    id = 2
    filtered = Author.objects.filter(id=id)

    # Obtener Los 10 primeros elementos
    limits  =Author.objects.all()[:10]

    # Obtener 5 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # Obtener todos Los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # Obtener todos Los elementos >= 15
    #* se usa -> campoBD(id, date, etc)__(especificador del operador) = 
    #! __lte -> lower than equals
    #! __gte -> greater than equals
    #! __lt -> lower than
    #! __gt -> greater than 
    #! __contains -> contiene
    #! __exact -> exacto

    orders = Author.objects.all().filter(id__lte = 5)

    #* Obtener todos los autores que tengan en su nombre la palabra yes
    
    filtered = Author.objects.filter(name__contains='yes')
    '''



    return render(request, "post/index.html", {'authors': authors, 'id': id})

def entries(request, id):
    author = Author.objects.get(id=id)
    entries = Entry.objects.filter(author=id)
    cont = entries.count()

    return render(request, "post/entries.html", {'author':author, 'entries':entries, 'cont':cont})

def info(request, idEntry):
    
    entry = Entry.objects.get(id=idEntry)

    return render(request, "post/info.html", {'entry':entry})

def author(request, id):
    author = Author.objects.get(id=id)

    return render(request, "post/author.html", {'author':author})

def update(request):
    author = Author.objects.get(id=8)
    author.name = "Felipe Gueche"
    author.save()
    return render(request, 'post/update.html', {})

def error(request, exception):
    return render(request, "post/404.html", status=404)