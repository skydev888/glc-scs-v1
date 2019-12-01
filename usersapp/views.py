from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm


class Top(generic.TemplateView):
    template_name = 'usersapp/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'usersapp/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_nme = 'usersapp/top.html'




# 自作登録
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'usersapp/top.html')
    else:
        form = SignUpForm()
    return render(request, 'usersapp/signup.html', {'form': form})