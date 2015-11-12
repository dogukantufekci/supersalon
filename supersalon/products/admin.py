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
        (_('Reminder Fields'), 
            {'fields': ('due_period', 'reminder_day_count_before_due_date', 'reminder_day_count_after_due_date',)}),
    )


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)