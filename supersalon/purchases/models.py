from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    # Date Fields
    service = models.PositiveSmallIntegerField(_("Service"), choices=SERVICES)


    class Meta:
        ordering = ('-visit', 'service',)
        verbose_name = _("Service Purchase")
        verbose_name_plural = _("Service Purchases")


    def __str__(self):
        return _("{customer} purchased {service}").format(customer=self.visit.customer, service=self.get_service_display())