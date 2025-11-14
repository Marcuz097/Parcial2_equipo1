# Create your views here.
# core/views.py

from django.shortcuts import render

def home_page(request):
    """
    Vista que maneja la página de inicio.
    """
    # Renderiza la plantilla que usará para la página de inicio.
    return render(request, 'core/base.html', {}) 