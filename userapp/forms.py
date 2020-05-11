from django import forms
from account.models import Account
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10, help_text='Required a valid modile numer')
    class Meta:
        model = Account
        fields = (
        'user_name',
        'mobile_number',
        #'user_type',
        'is_admin',
        'is_staff',
        'password1',
        'password2'
        )
