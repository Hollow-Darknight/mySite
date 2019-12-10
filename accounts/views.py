from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from myBlog import navigation


# Create your views here.
def profile(request):
    context = {

    }
    return render(request, 'accounts/profile.html', context)


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('characters')
        else:
            message = "Adresse mail ou mot de passe incorrecte."
            context = {
                'error': message
            }

            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confirmPass']:
            try:
                user = User.objects.get(username=request.POST['username'])
                email = User.objects.get(email=request.POST['email'])
                message = "Le nom d'utilisateur ou l'adresse email est déjà utilisé."
                context = {
                    'error': message
                }
                return render(request, 'accounts/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['confirmPass'], email=request.POST['email'])
                auth.login(request, user)
                message = "Bienvenue {}, vous êtes maintenant connecté !".format(request.POST['username'])
                return redirect('characters')
        else:
            message = "Les mots de passe ne correspondent pas."
            context = {
                'error': message
            }
            return render(request, 'accounts/signup.html', context)
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('characters')