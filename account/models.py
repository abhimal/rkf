from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, mobile_number, user_name, password=None):
        if not mobile_number:
            raise ValueError('user must have mobile nimber')
        if not user_name:
            raise ValueError('user must have username')

        user = self.model(mobile_number = mobile_number, user_name = user_name,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, user_name, password):
        user = self.create_user(mobile_number = mobile_number, password = password, user_name = user_name,)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=64)
    mobile_number = models.CharField(max_length=10, unique=True)
    user_type = models.CharField(max_length=64)
    email = models.EmailField(max_length=64,default="xyz@gmail.com")
    date_joined = models.DateTimeField(verbose_name='date joined',  auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',  auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['user_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True
