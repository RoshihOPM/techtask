from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm


admin.site.register(MenuItem, MenuItemAdmin)
