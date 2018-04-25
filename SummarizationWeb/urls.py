from django.conf.urls import url,re_path,include
from autosummarization import views

urlpatterns = [
    url(r'^$', views.index),
    re_path(r'autosummarization/',include('autosummarization.urls')),
]