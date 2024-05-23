from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreation
from .models import CustomUser
# Register your models here.
class UserAdminForm(UserAdmin):
    add_form = UserCreation
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'age']

admin.site.register( CustomUser,UserAdminForm)