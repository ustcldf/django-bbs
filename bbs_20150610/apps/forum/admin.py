from django.contrib import admin

# Register your models here.
from apps.forum.models import *


class ForumAdmin(admin.ModelAdmin):
    fields = ('district', 'name', 'description', 'moderators', 'icon')


admin.site.register(Forum, ForumAdmin)