from django.contrib import admin
from .models import Profile, Navigation, Content
# Register your models here.

admin.site.register(Navigation)
admin.site.register(Content)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "gender", "country", "email", "applied_at")