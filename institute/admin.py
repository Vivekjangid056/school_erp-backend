from django.contrib import admin
from .models import MainMenu, SubMenu, SuperSubMenu, InstituteRole, Permission, Institute

# Register MainMenu model
@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register SubMenu model
@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'menu')
    list_filter = ('menu',)
    search_fields = ('name',)

# Register SuperSubMenu model
@admin.register(SuperSubMenu)
class SuperSubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'submenu')
    list_filter = ('submenu',)
    search_fields = ('name',)

# Register InstituteRole model
# @admin.register(InstituteRole)
# class InstituteRoleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'is_active')
#     list_filter = ('is_active',)
#     search_fields = ('name',)
#     filter_horizontal = ('branches', 'menu',)

# Register Permission model
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'menu', 'submenu', 'supersubmenu')
    list_filter = ('role', 'menu', 'submenu', 'supersubmenu')
    search_fields = ('role__name',)

# Register Institute model if not already registered

