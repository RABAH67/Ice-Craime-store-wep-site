from django.contrib import admin
from .models import Products,custem ,Order,Cart
# Register your models here.


@admin.register(Products)
class ProductsModelAdmin(admin.ModelAdmin):
    
    list_display= ['id','title','selling_price','discoanted_price','category']


@admin.register(custem)
class custemModelAdmin(admin.ModelAdmin):
    
    list_display= ['id','user','locality','city','state']
    
    
admin.site.register(Order)
admin.site.register(Cart)