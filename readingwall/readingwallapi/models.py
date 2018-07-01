from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Wallposts(models.Model):
    owner = models.ForeignKey('auth.User', related_name='wallposts', on_delete=models.CASCADE)
    blog_url = models.CharField(max_length=255, blank=True)
    wall_context = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Connections(models.Model):
    PENDING = 0
    DONE = 1
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done'),
    )
    friendreq_by = models.ForeignKey('auth.User', related_name='requestedby', on_delete=models.CASCADE)
    friendreq_to = models.ForeignKey('auth.User', related_name='requestedto', on_delete=models.CASCADE)
    request_status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
