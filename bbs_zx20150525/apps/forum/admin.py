from django.contrib import admin

# Register your models here.
from apps.forum import models

admin.site.register(models.Forum)