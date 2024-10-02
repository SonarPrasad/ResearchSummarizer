from django.urls import path
from .views import register, user_login
from django.contrib.auth import views as auth_views
from summarizer import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home')
]