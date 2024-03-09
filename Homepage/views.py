from django.shortcuts import render, redirect

from django.urls import reverse
import json
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User


from .forms import LoginForm, ProfilePictureForm, RegisterForm
from django.http import JsonResponse

from .models import UserProfile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phonenumber']
        gender = request.POST['gender']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=pass1,
            first_name=first_name,
            last_name=last_name,

        )

        user.phone_number = phone_number
        user.gender = gender
        user.save()
        messages.success(request, "Your account has been created successfully")

        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request, login_successful=True):
    return render(request, 'Home.html', {'login_successful': login_successful})
def profile(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile_image = form.cleaned_data['profile_image']
            request.user.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = ProfilePictureForm()

    return render(request, 'profile.html', {'form': form})
def menu(request):
    return render(request, 'menu.html')

def cart(request):
    return render(request,'cart.html')

def user_logout(request):
    return render(request, 'login.html')

def res1(request):
    return render(request,'restaurant1.html')

def res2(request):
    return render(request,'restaurant2.html')

def res3(request):
    return render(request,'restaurant3.html')
def res4(request):
    return render(request,'restaurant4.html')
def res5(request):
    return render(request,'restaurant5.html')
def res6(request):
    return render(request,'restaurant6.html')
def res1cart(request):
    return render(request,'cart.html')
def res2cart(request):
    return render(request,'cart.html')
def res3cart(request):
    return render(request,'cart.html')

def res4cart(request):
    return render(request,'cart.html')
def res5cart(request):
    return render(request,'cart.html')
def res6cart(request):
    return render(request,'cart.html')
