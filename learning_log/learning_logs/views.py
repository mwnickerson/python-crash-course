from django.shortcuts import render

def index(request):
    """the home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

