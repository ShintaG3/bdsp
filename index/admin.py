from django.contrib import admin
from .models import Industry, ServiceCategory, Service, OrgBaseInfo
# Register your models here.
admin.site.register(Industry)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(OrgBaseInfo)
