from django.contrib import admin
from .models import *
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=("name","empid","departments","phone","working","address",)
    list_per_page=6

admin.site.register(Employee,EmpAdmin)
