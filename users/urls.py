from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
]