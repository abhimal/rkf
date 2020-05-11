from django.db import models
class Users_Tb(models.Model):
    user_name = models.CharField(max_length=64)
    mobile_number = models.CharField(max_length=10)
    psw = models.CharField(max_length=64)
    user_type = models.CharField(max_length=64)

    def __str__(self):#show tabel name on admin
        return self.user_name
