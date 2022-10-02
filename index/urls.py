from django.urls import path
from . import views

urlpatterns = [
    path('form', views.form, name='form'),
    path('', views.main, name='main'),
    path('<str:html>', views.main, name='main'),
]
