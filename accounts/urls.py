from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.my_account, name='profile'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout')
]