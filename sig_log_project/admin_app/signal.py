from user_app.models import Custom_User

from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import LogUser



@receiver(post_save, sender=Custom_User)
def log_user_activity(sender, instance, created, **kwargs):
    if created:
        activity = "Account Created"
    else:
        activity = "Account Updated"

    LogUser.objects.create(username=instance.username, activity=activity,phone_number=instance.phone_number,email=instance.email)
