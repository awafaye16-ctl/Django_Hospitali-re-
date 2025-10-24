from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from django.http import HttpResponse


def login_page(request):
    form = forms.LoginForm()
    message = ''
    
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')  # Redirection vers la page d'accueil
            else:
                message = 'Identifiants invalides,il vous reste 5 tentatives !!! '
                return render(request, 'blog/login.html', context={'form': form, 'message': message})
    
    return render(request, 'blog/login.html', context={'form': form, 'message': message})

@login_required
def accueil(request):
    """Vue pour la page d'accueil après connexion"""
    return render(request, 'blog/accueil.html')

def logout_view(request):
    """Vue pour la déconnexion"""
    logout(request)
    return redirect('login')