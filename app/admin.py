from django.contrib import admin
from app.models import Category, Item, Profile

admin.site.register([Profile, Category, Item])
