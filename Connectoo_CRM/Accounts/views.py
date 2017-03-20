from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserLoginForm
# from .models import 
from django.contrib.auth.models import User, Group
from CRM.models import Users

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