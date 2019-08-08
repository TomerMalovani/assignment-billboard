
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^get_post/$', views.get_post, name='get_post'),
    url(r'^create/$', views.create_new_post, name='create_new_post'),

]
