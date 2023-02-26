from django.shortcuts import render


def estaticos(request):
    return render(request, 'index.html', {})