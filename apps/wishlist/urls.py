from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_item$', views.add_item, name="add_item"),
    url(r'^create$', views.create, name="create"),
    url(r'^delete$', views.delete, name="delete"),
    url(r'^show/(?P<id>\d+)', views.show, name="show"),
    url(r'^add_wish$', views.add_wish, name="add_wish"),
]
