from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, "home.html", context = 
                {
                    'nome': 'a',
                })















def sobre(request):
    return HttpResponse("Sobre nós")

def receita(request):
    return HttpResponse("As receitas")
