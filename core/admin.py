from django.contrib import admin
from .models import Data
# Register your models here.
class AdminData(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'massage']

admin.site.register(Data, AdminData)