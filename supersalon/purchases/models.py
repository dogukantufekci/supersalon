from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductPurchase(models.Model):
    # Visit
    visit = models.ForeignKey('visits.Visit', 
        related_name='product_purchases',
        related_query_name='product_purchase',
        verbose_name=_("Visit"))
    # Product Fields
    product = models.ForeignKey('products.Product',
        related_name='product_purchases',
        related_query_name='product_purchase',
        verbose_name=_("Product"))
    amount = models.PositiveSmallIntegerField(_("Amount"), default=1)


    class Meta:
        unique_together = ('visit', 'product',)
        ordering = ('-visit', 'product',)
        verbose_name = _("Product Purchase")
        verbose_name_plural = _("Product Purchases")


    def __str__(self):
        return _("{customer} purchased {product}").format(customer=self.visit.customer, product=self.product.name)


class ServicePurchase(models.Model):
    # Visit
    visit = models.ForeignKey('visits.Visit', 
        related_name='service_purchases',
        related_query_name='service_purchase',
        verbose_name=_("Visit"))
    # Professional
    professional = models.ForeignKey('professionals.Professional', 
        related_name='service_purchases',
        related_query_name='service_purchase',
        verbose_name=_("Professional"))
    # Service Fields
    service = models.ForeignKey('services.Service',
        related_name='product_purchases',
        related_query_name='product_purchase',
        verbose_name=_("Service"))


    class Meta:
        unique_together = ('visit', 'service',)
        ordering = ('-visit', 'service',)
        verbose_name = _("Service Purchase")
        verbose_name_plural = _("Service Purchases")


    def __str__(self):
        return _("{customer} purchased {service}").format(customer=self.visit.customer, service=self.service.name)