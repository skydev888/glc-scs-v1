from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm


# 追加：myPage
def Mypage(request): #第一引数に django.http.request.HttpRequest を受け取る.戻り値に django.http.response.HttpResponse を返す
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'username' : form.cleaned_data.get('username'),
                'password' : form.cleaned_data.get('password1'),
                'email' : form.cleaned_data.get('email'),
            }
            return render(request, context, 'usersapp/mypage.html')
    else:
        form = SignUpForm()
    return render(request, 'usersapp/mypage.html', {'form': form})


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'usersapp/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_nme = 'usersapp/login.html'




# 追加：signup
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
            return render(request, 'usersapp/mypage.html')
    else:
        form = SignUpForm()
    return render(request, 'usersapp/signup.html', {'form': form})