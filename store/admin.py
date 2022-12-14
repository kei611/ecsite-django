from re import I
from django.contrib import admin
from .models import Product, Variation, ReviewRating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available'
        )
    prepopulated_fields = {'slug': ('product_name', )}
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active', )
    list_filter = ('product_name', 'variation_category', 'variation_value')

    

admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ReviewRating)