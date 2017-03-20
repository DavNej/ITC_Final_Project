from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserLoginForm
# from .models import 
from django.contrib.auth.models import User, Group
from CRM.models import Users


from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# class SettingsBackend(object):
#     """
#     Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

#     Use the login name and a hash of the password. For example:

#     ADMIN_LOGIN = 'admin'
#     ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
#     """

#     def authenticate(self, username=None, password=None):
#         login_valid = (username == username)
#         pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
#         if login_valid and pwd_valid:
        #     try:
        #         user = User.objects.get(username=username)
        #     except User.DoesNotExist:
        #         # Create a new user. There's no need to set a password
        #         # because only the password from settings.py is checked.
        #         user = User(username=username)
        #         user.is_staff = True
        #         user.is_superuser = True
        #         user.save()
        #     return user
        # return None
        # check_user = Users.objects.filter(email=email) 
        # if check_user.count() == 1:
        #     user = check_user.first()
        #     return user


    # def get_user(self, user_id):
    #     try:
    #         return Users.objects.get(pk=user_id)
    #     except Users.DoesNotExist:
    #         return None

def login_view(request):
    next = request.GET.get('next')
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # password = username
        user = authenticate(username=username, password=password)
        # user = (username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'Accounts/form.html', {'form':form, 'title':title})


def logout_view(request):
    logout(request)
    return redirect('/')