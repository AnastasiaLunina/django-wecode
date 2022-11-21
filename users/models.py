from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
# Creating a new model which will replicate fields from built in 
# User model. To avoid modifying User model directly. Make sure delete 
# Profile model and User model when user is deleted

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, 
                                      upload_to='profiles/', default="profiles/default_profile.jpg")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    # To diffirentiate sender and recipient related_name needs to be set, access the recipient field through the related name
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    email = models.EmailField(max_length=200, null=True, blank=False)
    is_read = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['is_read', '-created']
    

