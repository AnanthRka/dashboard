from django.contrib import admin
from .models import Cloud,VmRequest,VmReservation,PhysicalServerDetails,PhysicalServerCapacity,Storage,VmInventory,ApplicationInventory,ContactDetailsInventory
# Register your models here.
admin.site.register(Cloud)
admin.site.register(VmRequest)
admin.site.register(VmReservation)
admin.site.register(PhysicalServerDetails)
admin.site.register(PhysicalServerCapacity)
admin.site.register(Storage)
admin.site.register(VmInventory)
admin.site.register(ApplicationInventory)
admin.site.register(ContactDetailsInventory)