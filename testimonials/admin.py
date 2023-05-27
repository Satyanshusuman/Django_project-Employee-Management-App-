from django.contrib import admin
from .models import *
# Register your models here.

class TestiAdmin(admin.ModelAdmin):
    list_display=("Type","testimonial","picture","rating",)
    list_filter=("Type",)
    list_per_page=6

admin.site.register(Testimonial,TestiAdmin)