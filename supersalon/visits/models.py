from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Visit(models.Model):
    PAYMENT_METHODS = (
        (1, _("Cash")),
        (2, _("Credit Card")),
        (3, _("Cash and Credit Card")),
    )

    # Customer
    customer = models.ForeignKey('customers.Customer', verbose_name=_("Customer"))
    # Date Fields
    visit_date = models.DateField(_("Visit Date"), default=timezone.now)
    visit_time = models.TimeField(_("Visit Time"), blank=True, null=True)
    # Guest Fields
    female_guest_count = models.PositiveSmallIntegerField(_("Female Guest Count"), default=0)
    male_guest_count = models.PositiveSmallIntegerField(_("Male Guest Count"), default=0)
    child_guest_count = models.PositiveSmallIntegerField(_("Child Guest Count"), default=0)

    # Payment Fields
    payment_method = models.PositiveSmallIntegerField(_("Payment Method"), choices=PAYMENT_METHODS)
    total_payment_amount = models.DecimalField(_("Total Payment Amount"), decimal_places=2, max_digits=8)

    # Notes
    notes = models.TextField(_("Notes"), blank=True)


    class Meta:
        ordering = ('-visit_date',)
        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")


    def __str__(self):
        return _("{customer}'s Visit").format(customer=self.customer)