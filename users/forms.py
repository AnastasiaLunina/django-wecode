from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        for name, field in self.fields.items():
            # field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'id': 'id_title'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 
                  'email', 
                  'username', 
                  'location', 
                  'short_intro', 
                  'bio', 
                  'profile_image', 
                  'social_github', 
                  'social_twitter', 
                  'social_linkedin', 
                  'social_youtube',
                  'social_website'
                  ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

            field.widget.attrs.update({'id': 'id_title'})

        self.fields['profile_image'].widget.attrs.update({'id': 'id_featured_image', 'class': 'image-link'})
        self.fields['bio'].widget.attrs.update({'id': 'id_description'})
