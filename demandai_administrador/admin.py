from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'password', 'role', 'institution']


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['nome']

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
