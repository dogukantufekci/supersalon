from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import ServiceCategory, Service


class ServiceCategoryAdmin(admin.ModelAdmin):
	pass


class ServiceAdmin(admin.ModelAdmin):    
    list_display = (
        'name', 'category', 
        'price', 
        'due_period', 'reminder_day_count_before_due_date', 'remind_day_count_after_due_date',
    )
    list_filter = ('category',)
    search_fields = ('name',)
    fieldsets = (
        (_('Basic Profile'), {'fields': ('category', 'name',)}),
        (_('Price Fields'), {'fields': ('price',)}),
        (_('Reminder Fields'), 
        	{'fields': ('due_period', 'reminder_day_count_before_due_date', 'remind_day_count_after_due_date',)}),
    )


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)