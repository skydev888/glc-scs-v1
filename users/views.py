from django.http import HttpResponse

def Detail(request):
    str_out = "*** User detail page  ***<p />"
    str_out += "Wellcome to your mypage.<p />"
    return HttpResponse(str_out)


# 追加：ログイン機能
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm


class Top(generic.TemplateView):
    template_name = 'top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'top.html'


# 追加：サインアップページ
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'signup.html'