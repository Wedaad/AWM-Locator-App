# Register your models here.

from django.contrib.gis import admin
from .models import WorldBorder, UserProfile

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(UserProfile, admin.OSMGeoAdmin)
