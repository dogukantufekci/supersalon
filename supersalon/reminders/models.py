from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomerServiceReminderRel(models.Model):
	# Customer
	customer = models.ForeignKey('customers.Customer', verbose_name=_("Customer"))
	# Service
	service = models.ForeignKey('services.Service', verbose_name=_("Service"))
	# Professional
	last_professional = models.ForeignKey('professionals.Professional', verbose_name=_("Last Professional"))
	# Reminder Fields
	upcoming_reminder_date = models.DateField(_("Upcoming Service Due Reminder Date"))
	past_reminder_date = models.DateField(_("Past Service Due Reminder Date"))

	class Meta:
		unique_together = ('customer', 'service')
		ordering = ('upcoming_reminder_date',)
		verbose_name = _("CustomerServiceReminderRel")
		verbose_name_plural = _("CustomerServiceReminderRel")