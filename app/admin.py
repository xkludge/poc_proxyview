from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from app.repositories.models import AccountModel, UserModel


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_id')


class UserModelInline(admin.StackedInline):
    model = UserModel
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserModelInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(AccountModel, AccountModelAdmin)
