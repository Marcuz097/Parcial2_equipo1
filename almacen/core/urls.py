# core/urls.py (Si su vista real se llama 'index')

from django.urls import path
from . import views

urlpatterns = [
    # Cambia 'views.home_page' por 'views.index'
    path('', views.home_page, name='home'), 
]