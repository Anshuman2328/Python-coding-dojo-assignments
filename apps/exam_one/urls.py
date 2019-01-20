from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.main),
    url(r'^add$', views.add),
    url(r'^processadd$', views.processadd),
    url(r'^show/(?P<number>\d+)$', views.show),
    # url(r'^edit/(?P<id>\d+)$', views.edit),
    # url(r'^processedit/(?P<id>\d+)$', views.processedit),
    url(r'^delete/(?P<number>\d+)$', views.delete),
]