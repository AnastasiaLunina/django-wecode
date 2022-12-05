from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile
from django.conf import settings


# add event listeners 
# @receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    # print('Profile Saved')
    # print('Instance: ', instance)
    # print('Created: ', created)
    # print('Sender: ', sender)
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

        subject = "Thank you for regerester at WeCode!"
        message = 'We are very excited to learn more about you!'

        send_mail(
            subject, 
            message, 
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

def update_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save() 

# @receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    # print('Profile Deleted')
    # print('Instance: ', instance)
    # print('Sender: ', sender)
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=Profile)
post_delete.connect(delete_profile, sender=Profile)




