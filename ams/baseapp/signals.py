from .models import *
from django.contrib.auth import get_user_model
from .views import *
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()
@receiver(post_save, sender = User)
def create_user_profile(sender,instance, created, **kwargs):
    print("sender --> ", sender)
    print("Instance --> ", instance)
    print("Created --> ",created)
    if created:
        UserProfile.objects.create(user = instance)
        PersonalDetails.objects.create(user = instance)
        AcademicDetails.objects.create(user = instance)
        CategoryDetails.objects.create(user = instance)
        DocumentDetails.objects.create(user = instance)

