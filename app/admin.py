from django.contrib import admin
from app.models import Category, Item, Profile, Comment, Reply

admin.site.register([Profile, Category, Item, Comment, Reply])
