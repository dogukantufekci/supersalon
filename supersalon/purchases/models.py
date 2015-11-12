import datetime

from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from supersalon.reminders.models import CustomerServiceReminderRel, CustomerProductReminderRel


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
    # Notes
    discounted_unit_price = models.DecimalField(_("Discounted Unit Price"), decimal_places=2, max_digits=8, blank=True, null=True)
    discount_notes = models.TextField(_("Discount Notes"), blank=True)


    class Meta:
        unique_together = ('visit', 'service',)
        ordering = ('-visit', 'service',)
        verbose_name = _("Service Purchase")
        verbose_name_plural = _("Service Purchases")


    def __str__(self):
        return _("{customer} purchased {service}").format(customer=self.visit.customer, service=self.service.name)


@receiver([models.signals.post_save], sender=ServicePurchase)
def service_purchase_post_save(sender, instance, created, **kwargs):
    if instance.service.due_period:
        # Get dates
        due_date = instance.visit.visit_date + datetime.timedelta(days=instance.service.due_period)
        upcoming_reminder_date = due_date - datetime.timedelta(days=instance.service.reminder_day_count_before_due_date)
        past_reminder_date = due_date + datetime.timedelta(days=instance.service.reminder_day_count_after_due_date)
        # Update reminder dates or create new reminder
        try:
            reminder = CustomerServiceReminderRel.objects.get(
                customer=instance.visit.customer,
                service=instance.service)
            reminder.upcoming_reminder_date = upcoming_reminder_date
            reminder.past_reminder_date = past_reminder_date
            reminder.save()
        except:
            CustomerServiceReminderRel.objects.create(
                customer=instance.visit.customer,
                service=instance.service,
                upcoming_reminder_date=upcoming_reminder_date,
                past_reminder_date=past_reminder_date,
            )


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
    # Discount Fields
    discounted_unit_price = models.DecimalField(_("Discounted Unit Price"), decimal_places=2, max_digits=8, blank=True, null=True)
    discount_notes = models.TextField(_("Discount Notes"), blank=True)


    class Meta:
        unique_together = ('visit', 'product',)
        ordering = ('-visit', 'product',)
        verbose_name = _("Product Purchase")
        verbose_name_plural = _("Product Purchases")


    def __str__(self):
        return _("{customer} purchased {product}").format(customer=self.visit.customer, product=self.product.name)


@receiver([models.signals.post_save], sender=ProductPurchase)
def product_purchase_post_save(sender, instance, created, **kwargs):
    if instance.product.due_period:
        # Get dates
        due_date = instance.visit.visit_date + datetime.timedelta(days=instance.product.due_period)
        upcoming_reminder_date = due_date - datetime.timedelta(days=instance.product.reminder_day_count_before_due_date)
        past_reminder_date = due_date + datetime.timedelta(days=instance.product.reminder_day_count_after_due_date)
        # Update reminder dates or create new reminder
        try:
            reminder = CustomerProductReminderRel.objects.get(
                customer=instance.visit.customer,
                product=instance.product)
            reminder.upcoming_reminder_date = upcoming_reminder_date
            reminder.past_reminder_date = past_reminder_date
            reminder.save()
        except:
            CustomerProductReminderRel.objects.create(
                customer=instance.visit.customer,
                product=instance.product,
                upcoming_reminder_date=upcoming_reminder_date,
                past_reminder_date=past_reminder_date,
            )