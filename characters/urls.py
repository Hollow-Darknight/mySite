from django.urls import path

from characters import views

urlpatterns = [
    path('', views.all_characters, name='index'),
    path('characters/all/', views.all_characters, name="characters"),
]