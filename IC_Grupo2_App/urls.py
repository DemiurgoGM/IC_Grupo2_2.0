from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='IC_Grupo2_HomePage'),
    path('send', views.send, name='IC_Grupo2_Send'),
]
