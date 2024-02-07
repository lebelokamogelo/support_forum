from django.contrib.auth.forms import get_user_model
from django.forms import models

User = get_user_model()


class UserForm(models.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
