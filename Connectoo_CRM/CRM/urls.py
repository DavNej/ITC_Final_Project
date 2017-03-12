from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^schools/$', schools, name='schools'),
    url(r'^classes/$', classes, name='classes'),
    url(r'^classes_per_school/(?P<k_garden_id>[0-9]+)$', classes_per_school, name='classes_per_school'),
    url(r'^children/$', children, name='children'),
    url(r'^children_per_class/(?P<k_garden_id>[0-9]+)/(?P<group_id>[0-9]+)$', children_per_class, name='children_per_class'),
    url(r'^reports/$', reports, name='reports'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^attendances/$', attendances, name='attendances'),
    url(r'^contactPerson/$', contactPerson, name='contactPerson'),
]