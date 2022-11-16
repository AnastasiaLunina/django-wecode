from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


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

# @receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    # print('Profile Deleted')
    # print('Instance: ', instance)
    # print('Sender: ', sender)
    user = instance.user
    user.delete()

post_save.connect(create_profile, sender=User)
post_delete.connect(delete_profile, sender=Profile)




