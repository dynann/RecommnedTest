from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import CustomUser
class UserCreation(UserCreationForm):
    age = models.PositiveIntegerField(null=True, blank=True, editable=True)
    class Meta():
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'age')
        