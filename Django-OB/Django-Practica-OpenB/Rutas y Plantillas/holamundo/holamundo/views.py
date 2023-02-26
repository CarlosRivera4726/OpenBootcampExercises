from django.http import HttpResponse, HttpResponseRedirect

def saludo(request):
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("Adios!")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse(f"Hola {edad}")
    else:
        return HttpResponseRedirect("/admin/")