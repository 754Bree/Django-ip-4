from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import *
from django.http import Http404
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_hood = request.user.profile.hood
    posts = Post.objects.filter(neighborhood=current_hood.id).all()
    if current_hood == None:
        return redirect('complete')
    else:
        showing = Neighbourhood.objects.get(id=current_hood.id)
        return render(request, 'index.html', {'hood':showing, 'posts':posts})


@login_required(login_url='/accounts/login/')
def profile(request):    
    return render(request, 'registration/profile.html')


def business(request):
    current_hood = request.user.profile.hood
    business = Business.objects.filter(neighborhood=current_hood.id).all()
    return render(request, 'business.html', {'business':business})


def leave_neighbourhood(request):
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('hood')


def join(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'django_registration/registration_complete.html', {'hoods':hoods})

def join_btn(request, hood_id):
    selected_hood = Neighbourhood.objects.get(id=hood_id)
    if request.user.profile.hood == None:
        request.user.profile.hood = selected_hood
        request.user.profile.save()
        return redirect('home')
    else:
        return redirect('complete')