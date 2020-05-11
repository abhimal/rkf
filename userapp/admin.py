from django.contrib import admin
from userapp.models import Users_Tb
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','mobile_number','psw','user_type']

admin.site.register(Users_Tb, UsersAdmin)
