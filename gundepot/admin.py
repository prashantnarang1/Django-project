from django.contrib import admin
from gundepot.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','category','is_active']
    
    list_filter=['category','is_active']

    ordering=["id"]

admin.site.register(Product,ProductAdmin)
