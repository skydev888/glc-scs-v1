from django.urls import path
from . import views

app_name = 'usersapp'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup, name='signup'),
    path('mypage/', views.Mypage, name='mypage'),
]