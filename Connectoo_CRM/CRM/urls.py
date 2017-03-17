from django.conf.urls import url
from .views import *

app_name = 'CRM'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^schools_table/$', schools_table, name='schools_table'),
    url(r'^classes_table/$', classes_table, name='classes_table'),
    url(r'^classes_per_school/(?P<k_garden_id>[0-9]+)$', classes_per_school, name='classes_per_school'),
    url(r'^children/$', children, name='children'),
    url(r'^children_per_class/(?P<group_id>[0-9]+)$', children_per_class, name='children_per_class'),
    url(r'^reports/$', reports, name='reports'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^staff_table/$', staff_table, name='staff_table'),
    url(r'^attendances/$', attendances, name='attendances'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^gallery_kid/(?P<kid_id>[0-9]+)$', gallery_kid, name='gallery_kid'),
    url(r'^gallery_class/(?P<group_id>[0-9]+)$', gallery_class, name='gallery_class'),
    url(r'^gallery_schools/(?P<k_garden_id>[0-9]+)$', gallery_schools, name='gallery_schools'),
    url(r'^school_pictures/(?P<k_garden_id>[0-9]+)$', school_pictures, name='school_pictures'),
    url(r'^child_profile/(?P<kid_id>[0-9]+)$',child_profile, name='child_profile'),
    url(r'^add_to_album/$', add_to_album, name='add_to_album'),
    url(r'^child_profile_health/(?P<kid_id>[0-9]+)$', child_profile_health, name='child_profile_health'),
    url(r'^child_profile_reports/(?P<kid_id>[0-9]+)$', child_profile_reports, name='child_profile_reports'),
    url(r'^calendar/$', calendar, name='calendar'),
]