from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^schools/$', schools, name='schools'),
    url(r'^schools_table/$', schools_table, name='schools_table'),
    url(r'^classes_table/$', classes_table, name='classes_table'),
    url(r'^classes_per_school/(?P<k_garden_id>[0-9]+)$', classes_per_school, name='classes_per_school'),
    url(r'^children/$', children, name='children'),
    url(r'^children_per_class/(?P<group_id>[0-9]+)$', children_per_class, name='children_per_class'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^reports/$', reports, name='reports'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^staff_table/$', staff_table, name='staff_table'),
    url(r'^attendances/$', attendances, name='attendances'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^gallery_per_kid/$', gallery_per_kid, name='gallery_per_kid'),
    url(r'^gallery_per_class/$', gallery_per_class, name='gallery_per_class'),
    url(r'^child_profile/(?P<kid_id>[0-9]+)$',child_profile, name='child_profile'),
    url(r'^child_profile_contact/$', child_profile_contact, name='child_profile_contact'),
    url(r'^child_profile_medical/$', child_profile_medical, name='child_profile_medical'),
    url(r'^child_profile_reports/$', child_profile_reports, name='child_profile_reports'),
]