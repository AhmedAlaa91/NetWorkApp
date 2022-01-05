from django.contrib import admin

# Register your models here.
from .models import vlan , ips , subnet

admin.site.register (vlan)
admin.site.register (subnet)
admin.site.register (ips)