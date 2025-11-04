from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutMe.html', views.about_me, name='about'),
]
