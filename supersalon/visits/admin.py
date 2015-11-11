from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from supersalon.purchases.models import ProductPurchase, ServicePurchase

from .models import Visit



class ServicePurchaseInlineAdmin (admin.TabularInline):
    """Inline configuration for Django's admin on the ServicePurchase model."""
    model = ServicePurchase
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


class ProductPurchaseInlineAdmin (admin.TabularInline):
    """Inline configuration for Django's admin on the ProductPurchase model."""
    model = ProductPurchase
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


class VisitAdmin(admin.ModelAdmin):    
    list_display = (
        'customer', 'visit_date', 'arrival_time', 'departure_time', 'str_service_purchases', 'str_product_purchases', 'total_payment_amount', 'notes',
    )
    list_filter = ('visit_date', 'arrival_time', 'departure_time',)
    search_fields = ('customer__name',)
    fieldsets = (
        (_('Customer'), {'fields': ('customer',)}),
        (_('Date Fields'), {'fields': ('visit_date', 'arrival_time', 'departure_time')}),
        (_('Guest Fields'), {'fields': ('female_guest_count', 'male_guest_count', 'child_guest_count')}),
        (_('Payment Fields'), {'fields': ('payment_method', 'total_payment_amount',)}),
        (_('Notes'), {'fields': ('notes',)}),
    )
    inlines = (ServicePurchaseInlineAdmin, ProductPurchaseInlineAdmin,)
    raw_id_fields = ('customer',)
    autocomplete_lookup_fields = {
        'fk': ['customer'],
    }


admin.site.register(Visit, VisitAdmin)