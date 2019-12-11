from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

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
            messages.success(request, "<strong>Bonjour {}</strong>, vous êtes maintenant connecté !".format(request.POST['username']))
            return redirect('home')
        else:
            messages.error(request, "<strong>Attention : </strong>Adresse mail ou mot de passe incorrecte.")
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confirmPass']:
            try:
                user = User.objects.get(username=request.POST['username'])
                email = User.objects.get(email=request.POST['email'])
                messages.error(request, "<strong>Attention : </strong>Le nom d'utilisateur ou l'adresse email est "
                                        "déjà utilisé.")
                return render(request, 'accounts/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['confirmPass'],
                                                email=request.POST['email'])
                auth.login(request, user)
                messages.success(request, "<strong>Bienvenue {}</strong>, vous êtes maintenant connecté !".format(request.POST['username']))
                return redirect('home')
        else:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Vous avez bien été déconnecté")
        return redirect('home')