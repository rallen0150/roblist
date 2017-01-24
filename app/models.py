from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#For Token
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    image = models.FileField(null=True, blank=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://dhqbrvplips7x.cloudfront.net/webchat/1.0.23/agent-e202505f.png"

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)

class Category(models.Model):
    item_type = models.CharField(max_length=255)

    def __str__(self):
        return self.item_type

class Item(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=300)
    picture = models.FileField(null=True, blank=True)
    category = models.ForeignKey(Category)
    price = models.FloatField(null=True, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "https://dhqbrvplips7x.cloudfront.net/webchat/1.0.23/agent-e202505f.png"
