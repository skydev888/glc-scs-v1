from django.urls import path
from . import views


urlpatterns = [
    path('detail', views.Detail, name='detail'),
    path('', views.Top.as_view(), name='top'),
    path('top/', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
]