from django.urls import path
from . import views

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'submit/', views.submit, name='submit'),
]