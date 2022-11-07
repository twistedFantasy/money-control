from django.contrib import admin

from leprechaun.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
