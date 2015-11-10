from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import  ProductPurchase, ServicePurchase


class ProductPurchaseAdmin(admin.ModelAdmin):    
    pass

class ServicePurchaseAdmin(admin.ModelAdmin):    
    pass


admin.site.register(ProductPurchase, ProductPurchaseAdmin)
admin.site.register(ServicePurchase, ServicePurchaseAdmin)