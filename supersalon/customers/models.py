from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    GENDERS = (
        ('u', _("Unknown")),
        ('f', _("Female")),
        ('m', _("Male")),
    )

    RELATIONSHIP_STATUSES = (
        ('u', _("Unknown")),
        ('s', _("Single")),
        ('e', _("Engaged")),
        ('m', _("Married")),
    )

    # Basic Profile
    photo = models.ImageField(_("Photo"), max_length=255, upload_to='customers', default='customers/placeholder.jpg')
    name = models.CharField(_("Name"), max_length=255)
    birth_date = models.DateField(_("Birth Date"), blank=True, null=True)
    gender = models.CharField(_("Gender"), choices=GENDERS, default='u', max_length=1)
    # Contact Info
    mobile_phone_number = PhoneNumberField(_("Mobile Phone Number"), blank=True)
    email = models.EmailField(_("E-mail"), blank=True)
    # Relationship Info
    relationship_status = models.CharField(_("Relationship Status"), choices=RELATIONSHIP_STATUSES, max_length=1, default='u')
    # Special Dates
    engagement_date = models.DateField(_("Engagement Date"), blank=True, null=True)
    wedding_date = models.DateField(_("Wedding Date"), blank=True, null=True)
    # Newspaper
    newspaper = models.CharField(_("Newspaper"), blank=True, max_length=128)
    # Magazine
    magazine = models.CharField(_("Magazine"), blank=True, max_length=128)
    # Drink
    drink = models.CharField(_("Drink"), blank=True, max_length=128)
    # Notes
    notes = models.TextField(_("Notes"), blank=True)
    # Visits
    last_visit = models.DateField(_("Last Visit"), blank=True, null=True)


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)


    class Meta:
        ordering = ('name',)
        verbose_name = _("Customer")
        verbose_name_plural = _("Customer")


    def __str__(self):
        return _("{name} ({gender}-{age})").format(name=self.name, gender=self.get_gender_display()[0], age=self.get_age())


    def admin_photo(self):
        return '<img style="max-height:100px; max-width:100px;" src="%s"/>' % self.photo.url
    admin_photo.allow_tags = True

    def get_age(self):
        if self.birth_date is None:
            return 0
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))