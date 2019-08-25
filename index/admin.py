from django.contrib import admin
from .models import Industry, ServiceCategory, Service, OrgBaseInfo, Case, Experience
# Register your models here.
admin.site.register(Industry)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(OrgBaseInfo)
admin.site.register(Case)
admin.site.register(Experience)
