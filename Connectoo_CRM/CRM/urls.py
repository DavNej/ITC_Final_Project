from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^schools/$', views.schools, name='schools'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^children/$', views.children, name='children'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^attendances/$', views.attendances, name='attendances'),
    url(r'^contactPerson/$', views.contactPerson, name='contactPerson'),
]