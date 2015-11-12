from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomerServiceReminderRel(models.Model):
	# Customer
	customer = models.ForeignKey('customers.Customer', verbose_name=_("Customer"))
	# Service
	service = models.ForeignKey('services.Service', verbose_name=_("Service"))
	# Reminder Fields
	upcoming_reminder_date = models.DateField(_("Upcoming Service Due Reminder Date"))
	past_reminder_date = models.DateField(_("Past Service Due Reminder Date"))


	class Meta:
		unique_together = ('customer', 'service')
		ordering = ('upcoming_reminder_date',)
		verbose_name = _("Customer Service Reminder Rel")
		verbose_name_plural = _("Customer Service Reminder Rels")


	def __str__(self):
		return _("{0} - {1} Reminder Rel").format(self.customer, self.service)


class CustomerProductReminderRel(models.Model):
	# Customer
	customer = models.ForeignKey('customers.Customer', verbose_name=_("Customer"))
	# Product
	service = models.ForeignKey('products.Product', verbose_name=_("Product"))
	# Reminder Fields
	upcoming_reminder_date = models.DateField(_("Upcoming Product Due Reminder Date"))
	past_reminder_date = models.DateField(_("Past Product Due Reminder Date"))


	class Meta:
		unique_together = ('customer', 'service')
		ordering = ('upcoming_reminder_date',)
		verbose_name = _("Customer Product Reminder Rel")
		verbose_name_plural = _("Customer Product Reminder Rels")


	def __str__(self):
		return _("{0} - {1} Reminder Rel").format(self.customer, self.product)