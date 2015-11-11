from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
	pass


class ProductAdmin(admin.ModelAdmin):    
    list_display = (
        'name', 'category', 'price',
    )
    list_filter = ('category',)
    search_fields = ('name',)
    fieldsets = (
        (_('Basic Profile'), {'fields': ('category', 'name',)}),
        (_('Price Fields'), {'fields': ('price',)}),
    )


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)