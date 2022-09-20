from django.contrib import admin
from django.contrib.auth.models import Group

from leprechaun.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


admin.site.unregister(Group)
