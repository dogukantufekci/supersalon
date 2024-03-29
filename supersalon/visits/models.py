from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


from supersalon.purchases.models import ServicePurchase, ProductPurchase


class Visit(models.Model):
    # Customer
    customer = models.ForeignKey('customers.Customer', verbose_name=_("Customer"))
    # Date Fields
    visit_date = models.DateField(_("Visit Date"), default=timezone.now)
    arrival_time = models.TimeField(_("Arrival Time"), blank=True, null=True)
    departure_time = models.TimeField(_("Departure Time"), blank=True, null=True)
    # Guest Fields
    female_guest_count = models.PositiveSmallIntegerField(_("Female Guest Count"), default=0)
    male_guest_count = models.PositiveSmallIntegerField(_("Male Guest Count"), default=0)
    child_guest_count = models.PositiveSmallIntegerField(_("Child Guest Count"), default=0)

    # Payment Fields
    total_payment_amount = models.DecimalField(_("Total Payment Amount"), decimal_places=2, max_digits=8)

    # Notes
    notes = models.TextField(_("Notes"), blank=True)


    class Meta:
        ordering = ('-visit_date',)
        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")


    def __str__(self):
        return _("{customer}'s Visit").format(customer=self.customer)


    def str_product_purchases(self):
        x = ""
        for product_purchase in self.product_purchases.all():
            x += "%s, " % product_purchase.product.name
        return x 


    def str_service_purchases(self):
        x = ""
        for service_purchase in self.service_purchases.all():
            x += "%s, " % service_purchase.service.name
        return x


@receiver([models.signals.post_save], sender=Visit)
def visit_post_save(sender, instance, created, **kwargs):
    # Update Customer last_visit
    last_visit = Visit.objects.latest('visit_date')
    instance.customer.last_visit = last_visit.visit_date
    instance.customer.save()
    # Send SMS to thank for the visit