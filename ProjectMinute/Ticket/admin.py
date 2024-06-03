from django.contrib import admin
from .models import State_Master,User_Master
# Register your models here.

@admin.register(User_Master)
class UserMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'email', 'phone', 'city', 'joining_date', 'state']

@admin.register(State_Master)
class StateMasterAdmin(admin.ModelAdmin):
    list_display = ['state_name', 'state_code']