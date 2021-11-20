from django.contrib import admin
from django.urls import path, include
from app_osrm.views import home, lista, form, create, view
from app_usuarios.views import cadastro, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('lista/', lista, name="lista"),
    path('form/', form, name="form"),
    path('create/', create, name="create"),
    path('view/<int:pk>', view, name="view"),
    path('view/<int:pk>', view, name="view"),
    path('', include("app_usuarios.urls")),
    path('login/', login, name="login"),
    path('cadastro/', cadastro, name="cadastro"),
]
