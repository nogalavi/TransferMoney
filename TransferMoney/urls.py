from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getoffer', views.get_offer, name='get_offer'),
]