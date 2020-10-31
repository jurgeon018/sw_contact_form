from django import apps 
from django.utils.translation import gettext_lazy as _ 

class ContactConfig(apps.AppConfig):
    name = 'sw_contact_form'
    verbose_name = _('Зворотній звязок')
    verbose_name_plural = verbose_name

default_app_config = 'sw_contact_form.ContactConfig'


