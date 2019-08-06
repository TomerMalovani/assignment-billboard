
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.get_activities, name='get_activites'),
    url(r'^login', login, name='login'),
    url(r'^logout', logout, name='logout')
]
