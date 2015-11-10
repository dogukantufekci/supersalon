from django.db import models
from django.utils.translation import ugettext_lazy as _


class Professional(models.Model):
    # User
    user = models.OneToOneField('users.User', primary_key=True)


    class Meta:
        ordering = ('user__first_name', 'user__last_name',)
        verbose_name = _("Professional")
        verbose_name_plural = _("Professionals")


    def __str__(self):
        return _("Professional {user_full_name}").format(user_full_name=self.user.get_full_name())