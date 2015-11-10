from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    GENDERS = (
        ('f', _("Female")),
        ('m', _("Male")),
    )

    # Basic Profile
    photo = models.ImageField(_("Photo"), max_length=255, upload_to='customers', default='customers/placeholder.jpg')
    name = models.CharField(_("Name"), max_length=255)
    birth_date = models.DateField(_("Birth Date"), blank=True)
    gender = models.CharField(_("Gender"), blank=True, choices=GENDERS, max_length=1)
    # Contact Info
    mobile_phone_number = PhoneNumberField(_("Mobile Phone Number"), blank=True)
    email = models.EmailField(_("Email"), blank=True)
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
        return _("{name} ({gender}{age})").format(name=self.name, gender=self.get_gender_display()[0], age=self.get_age())


    def admin_photo(self):
        return '<img style="max-height:100px; max-width:100px;" src="%s"/>' % self.photo.url
    admin_photo.allow_tags = True

    def get_age(self):
        if self.birth_date is None:
            return 0
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))