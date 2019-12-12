from django.urls import path

from characters import views

urlpatterns = [
    path('', views.all_characters, name='characters'),
    path('all/', views.all_characters, name='characters-all'),
    path('details/<slug:slug>/', views.character_details, name='character-details'),
    path('details/<slug:slug>/<str:message>/', views.character_details, name='character-details-message'),
    path('details/<slug:slug>/edit/<int: post_id>/', views.edit_comment, name='edit-comment')
]