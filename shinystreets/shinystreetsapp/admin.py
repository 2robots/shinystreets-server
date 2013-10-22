from django.contrib import admin
from .models import Area, Issue, User

class AreaAdmin(admin.ModelAdmin):
	prepopulated_fields = {}

class IssueAdmin(admin.ModelAdmin):
	prepopulated_fields = {}

class UserAdmin(admin.ModelAdmin):
	prepopulated_fields = {}

admin.site.register(Area, AreaAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(User, UserAdmin)