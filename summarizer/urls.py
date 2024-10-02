from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('ask/', views.ask_question, name='ask_question'),
    path('create-word/', views.create_word, name='create_word'),
    path('download_file/<str:file_name>/', views.download_file, name='download_file'),
    path('about/', views.about, name='about'),
]