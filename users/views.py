from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Profile, Message
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import search_profiles, paginate_profiles

# Create your views here.
def profiles(request):
    profiles, search_query = search_profiles(request)

    custom_range, profiles = paginate_profiles(request, profiles, 2)
    
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range,
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
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def user_register(request):
    page = 'register'
    # accessing the data from model
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
    # getting particular user
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


@login_required(login_url='login')
def add_skill(request):
    # getting particular user
    profile = request.user.profile

    # accessing the data from model
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Good job adding a new skill!')
            return redirect('account')

    # passing to context to render it in a template
    context = {
        'form': form,
    }
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def edit_skill(request, pk):
    # accessing the data from model
    profile = request.user.profile
    # Make sure only owner can edit it
    skill = profile.skill_set.get(id=pk)
    # Add instance=profile as an argument to pre-render user's information in form
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        # getting particular user
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated!')            
            return redirect('account')
    # passing to context to render it in a template
    context = {
        'form': form,
    }
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted!')            
        return redirect('account')

    context = {
        # to use delete_template throughout the project key should be 'object'
        'object': skill,
    }

    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox(request):
    # getting currently logged in user
    profile = request.user.profile
    # getting messages from model's related_name
    all_messages = profile.messages.all()
    unread_count = all_messages.filter(is_read=False).count()

    context = {
        'all_messages': all_messages,
        'unread_count': unread_count,
    }
    
    return render(request, 'users/inbox.html', context)
