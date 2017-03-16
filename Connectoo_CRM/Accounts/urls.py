from django.conf.urls import url
# from . import views
from django.contrib.auth import views as authviews
from Accounts.views import login_view, logout_view

app_name = 'accounts'
urlpatterns = [
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
]
