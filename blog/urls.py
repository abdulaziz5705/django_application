from django.urls import path
from .views import home, login, regester

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('regester/', regester, name='regester'),
]
