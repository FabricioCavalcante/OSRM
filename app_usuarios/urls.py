from django.contrib import admin
from django.urls import path
from . import views
#from app_osrm.views import home, lista, form, create, view

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]