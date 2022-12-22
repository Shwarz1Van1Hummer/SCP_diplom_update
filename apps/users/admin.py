from django.contrib import admin

from .models import CustomUser, NewsUsers

admin.site.register(CustomUser)
admin.site.register(NewsUsers)
