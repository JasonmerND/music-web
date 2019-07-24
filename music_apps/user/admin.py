from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username','mobile','qq','weChat','email']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (
        _('Personal info'),
        {
            'fields':(
                'first_name',
                'last_name',
                'email',
                'mobile',
                'qq',
                'weChat'
            )
        }
    )
