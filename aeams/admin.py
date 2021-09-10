from django.contrib import admin
from django.contrib.auth.models import Group #, Permission
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import TblUsers as User

class UserAdmin(BaseUserAdmin):
    # add_form =  UserCreationForm
    list_display = ('login', 'name', 'role_id')
    # list_filter = ('role_id',)
    # fieldsets = (
    #     (None, {'fields': ('login', 'name','password')}),
    #
    #     ('Permissions', {'fields': ('role_id',)}),
    # )
    # search_fields =  ('login', 'name')
    # ordering = ('login','name')
    search_fields =  ()
    ordering = ()

    filter_horizontal = ()
    list_filter = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# admin.site.unregister(Permission)