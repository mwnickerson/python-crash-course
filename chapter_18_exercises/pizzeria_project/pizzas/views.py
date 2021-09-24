from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """the home page for pizzas"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """show all pizzas"""
    pizzas = Pizza.objects.
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html')