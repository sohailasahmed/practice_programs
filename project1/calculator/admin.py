from django.contrib import admin
from calculator.models import Laptop

class NewsAdmin(admin.ModelAdmin):
    list_display=('Laptop_name','Laptop_desc',"Laptop_img")

admin.site.register(Laptop,NewsAdmin)
# Register your models here.
