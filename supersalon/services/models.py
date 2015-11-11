from django.db import models
from django.utils.translation import ugettext_lazy as _


class ServiceCategory(models.Model):
	name = models.CharField(_("Name of Service Category"), max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = _("Service Category")
		verbose_name_plural = _("Service Categories")

	def __str__(self):
		return self.name


class Service(models.Model):
	category = models.ForeignKey('services.ServiceCategory', 
		related_name='services', 
		related_query_name='service', 
		verbose_name=_("Service Category"))
	name = models.CharField(_("Name of Service"), max_length=255)
	price = models.DecimalField(_("Price"), decimal_places=2, max_digits=8)
	due_period = models.PositiveSmallIntegerField(_("Due Period (in days)"), blank=True, null=True)
	# reminders
	reminder_day_count_before_due_date = models.PositiveSmallIntegerField(_("Reminder Day Count Before Due Date"), default=2)
	remind_day_count_after_due_date = models.PositiveSmallIntegerField(_("Reminder Day Count Before After Date"), default=10)

	class Meta:
		unique_together = ('category', 'name')
		ordering = ('category', 'name')
		verbose_name = _("Service")
		verbose_name_plural = _("Services")

	def __str__(self):
		return "{0} ({1})".format(self.name, self.category.name)