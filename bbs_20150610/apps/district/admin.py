from django.contrib import admin
from apps.district.models import *


class DistrictAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'moderators')


admin.site.register(District, DistrictAdmin)