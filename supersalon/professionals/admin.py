from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Professional


class ProfessionalAdmin(admin.ModelAdmin):    
    pass


admin.site.register(Professional, ProfessionalAdmin)