from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/<int:id>/', views.detalhe_evento, name="detalhe_evento"),
    path('local/<int:id>/', views.local, name="local")
]