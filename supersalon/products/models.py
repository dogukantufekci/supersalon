from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductCategory(models.Model):
	name = models.CharField(_("Name of Product Category"), max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = _("Product Category")
		verbose_name_plural = _("Product Categories")

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey('products.ProductCategory', 
		related_name='products',
        related_query_name='product',
		verbose_name=_("Product Category"))
	name = models.CharField(_("Name of Product"), max_length=255)
	price = models.DecimalField(_("Price"), decimal_places=2, max_digits=8)
	due_period = models.PositiveSmallIntegerField(_("Due Period (in days)"), blank=True, null=True)
	# reminders
	reminder_day_count_before_due_date = models.PositiveSmallIntegerField(_("Reminder Day Count Before Due Date"), default=2)
	reminder_day_count_after_due_date = models.PositiveSmallIntegerField(_("Reminder Day Count Before After Date"), default=12)

	
	class Meta:
		unique_together = ('category', 'name')
		ordering = ('category', 'name')
		verbose_name = _("Product")
		verbose_name_plural = _("Products")

	def __str__(self):
		return "{0} ({1})".format(self.name, self.category.name)