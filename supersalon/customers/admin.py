from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):    
    list_display = (
        'admin_photo', 'name', 'get_age', 'birth_date', 'gender', 'mobile_phone_number', 'email', 'last_visit',
    )
    list_filter = ('gender',)
    search_fields = ('name',)
    fieldsets = (
        (_('Basic Profile'), {'fields': ('photo', 'name', 'birth_date', 'gender')}),
        (_('Contact Info'), {'fields': ('mobile_phone_number', 'email')}),
        (_('Relationship Fields'), {'fields': ('relationship_status', 'engagement_date', 'wedding_date',)}),
        (_('Preference Fields'), {'fields': ('newspaper', 'magazine', 'drink',)}),
        (_('Notes'), {'fields': ('notes',)}),
        (_('Visits'), {'fields': ('last_visit',)}),
    )


admin.site.register(Customer, CustomerAdmin)