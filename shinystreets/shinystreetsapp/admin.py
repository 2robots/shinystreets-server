from django.contrib import admin
from .models import Area

class AreaAdmin(admin.ModelAdmin):
	prepopulated_fields = {}

admin.site.register(Area, AreaAdmin)