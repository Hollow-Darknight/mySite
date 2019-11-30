from django.urls import path

from home import views

urlpatterns = [
    path('', views.landpage, name='index'),
    path('home/', views.homepage, name='home')
]