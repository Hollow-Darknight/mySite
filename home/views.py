from django.shortcuts import render, get_object_or_404


def landpage(request):
    return render(request, 'index.html')


def homepage():
    return None