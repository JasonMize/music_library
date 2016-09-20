from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    # url(r'^music/(?P<id>\d+)/$', views.artists, name='detail'),
]




