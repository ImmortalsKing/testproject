from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['title']
    }

    list_display = ['title', 'price' , 'brand' , 'is_active' , 'is_delete']
    list_filter = ['category' , 'brand' , 'is_active']
    list_editable = ['price' , 'is_active']

admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductTag)