from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')

def a_propos(request):
    return render(request, 'a_propos.html')

def contact(request):
    return render(request, 'contact.html')