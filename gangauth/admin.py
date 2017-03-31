from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gangauth.models import User
from django.utils.translation import ugettext as _


class UserGangAdmin(UserAdmin):
    readonly_fields = ['last_login', 'date_joined']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('profil_picture', 'first_name', 'last_name', 'sex', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserGangAdmin)
