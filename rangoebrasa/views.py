from django.shortcuts import render, HttpResponse
from .models import Menu

def dashborad(request):
    dados = {
        "dados": Menu.objects.all()
    }
    return render(request, 'rangoebrasa/dashboard.html', context=dados)