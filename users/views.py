from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills_with_description = profile.skill_set.exclude(description__exact="")
    skills_without_description = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'skills_with_description': skills_with_description,
        'skills_without_description': skills_without_description,
    }
    return render(request, 'users/user-profile.html', context)


def user_login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def user_register(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # creating a new instance and saving it temporary to make changes to that instance
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            messages.info(request, 'User account was created!')

            login(request, user)
            return redirect('edit-profile')
        
        else:
            messages.error(request, 'Oh no, something went wrong')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def get_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }
    
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    # Add instance=profile as an argument to pre-render user's information in form
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        # To send image the request.FILES needed
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {
        'form': form,
    }

    return render(request, 'users/edit_profile_form.html', context)