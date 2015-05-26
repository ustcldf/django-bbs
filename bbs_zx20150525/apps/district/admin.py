from django.contrib import admin

# Register your models here.
from apps.district import models

admin.site.register(models.District)