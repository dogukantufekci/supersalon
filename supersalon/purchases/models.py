from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductPurchase(models.Model):
    PRODUCTS = (
        (0, _('Other')),
        (_('Nashi Argan'), (
                (1001, 'Color #2543 (Nashi Argan)'),
                (1002, 'Color #1231 (Nashi Argan)'),
            )
        ),
        (_('Schwarzkopf'), (
                (2001, 'Color #2543 (Schwarzkopf)'),
                (2002, 'Color #1231 (Schwarzkopf)'),
            )
        ),
    )

    # Visit
    visit = models.ForeignKey('visits.Visit', verbose_name=_("Visit"))
    # Product Fields
    product = models.PositiveSmallIntegerField(_("Product"), choices=PRODUCTS)
    count = models.PositiveSmallIntegerField(_("Count"), default=1)


    class Meta:
        unique_together = ('visit', 'product',)
        ordering = ('-visit', 'product',)
        verbose_name = _("Product Purchase")
        verbose_name_plural = _("Product Purchases")


    def __str__(self):
        return _("{customer} purchased {product}").format(customer=self.visit.customer, product=self.get_product_display())


class ServicePurchase(models.Model):
    SERVICES = (
        (0, _('Other')),
        (_('Hair (Woman)'), (
                (101, 'Hair Cut'),
                (102, 'Hair Coloring'),
            )
        ),
        (_('Nail (Woman)'), (
                (201, 'Manicure'),
                (202, 'Pedicure'),
            )
        ),
    )

    # Visit
    visit = models.ForeignKey('visits.Visit', verbose_name=_("Visit"))
    # Professional
    professional = models.ForeignKey('professionals.Professional', verbose_name=_("Professional"))
    # Service Fields
    service = models.PositiveSmallIntegerField(_("Service"), choices=SERVICES)


    class Meta:
        unique_together = ('visit', 'service',)
        ordering = ('-visit', 'service',)
        verbose_name = _("Service Purchase")
        verbose_name_plural = _("Service Purchases")


    def __str__(self):
        return _("{customer} purchased {service}").format(customer=self.visit.customer, service=self.get_service_display())