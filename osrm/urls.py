from django.contrib import admin
from django.urls import path
from app_osrm.views import home, lista, form, create, view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('lista/', lista, name="lista"),
    path('form/', form, name="form"),
    path('create/', create, name="create"),
    path('view/<int:pk>', view, name="view"),
]
