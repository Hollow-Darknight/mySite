from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from myBlog import navigation


# Create your views here.
def my_account(request):
    return None


def login(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_LOGIN),
    }

    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confirmPass']:
            try:
                user = User.objects.get(username=request.POST['username'])
                email = User.objects.get(email=request.POST['email'])
                message = "Le nom d'utilisateur ou l'adresse email est déjà utilisé."
                context = {
                    'navigation_items': navigation.navigation_items(navigation.NAV_SIGNUP),
                    'error': message
                }
                return render(request, 'accounts/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['confirmPass'], email=request.POST['email'])
                auth.login(request, user)
                message = "Bienvenue {}, vous êtes maintenant connecté !".format(request.POST['username'])
                return redirect('characters', message)
    else:
        context = {
            'navigation_items': navigation.navigation_items(navigation.NAV_SIGNUP)
        }
        return render(request, 'accounts/signup.html', context)


def logout(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_LOGOUT),
    }

    return render(request, 'accounts/login.html', context)
