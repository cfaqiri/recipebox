from django.contrib import admin
from recipes.models import Recipe, User

admin.site.register(User)
admin.site.register(Recipe)