from django.contrib import admin
from .models import Message
# Register your models here.

admin.site.register(Message)

from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy

admin.site.site_header = 'Umesh Atomy Admin'
    
AdminSite.site_title = 'Umesh Atomy Admin'
