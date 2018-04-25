from django.conf.urls import url
from autosummarization import views

urlpatterns = [
    url(r'^index/$', views.index,name = 'index'),
    url(r'^submit/$', views.submit,name = 'submit'),
]