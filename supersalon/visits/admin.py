from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Visit


class VisitAdmin(admin.ModelAdmin):    
    list_display = (
        'customer', 'visit_date', 'visit_time', 'total_payment_amount', 'notes',
    )
    list_filter = ('visit_date', 'visit_time',)
    search_fields = ('customer__name',)
    fieldsets = (
        (_('Customer'), {'fields': ('customer',)}),
        (_('Date Fields'), {'fields': ('visit_date', 'visit_time')}),
        (_('Guest Fields'), {'fields': ('female_guest_count', 'male_guest_count', 'child_guest_count')}),
        (_('Payment Fields'), {'fields': ('payment_method', 'total_payment_amount',)}),
        (_('Notes'), {'fields': ('notes',)}),
    )


admin.site.register(Visit, VisitAdmin)