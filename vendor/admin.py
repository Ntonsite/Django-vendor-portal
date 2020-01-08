from django.contrib import admin

# Register your models here.
from .models import Vendor, Contract, License

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendorName', 'contactPerson', 'service','locationAddress')
admin.site.register(Vendor, VendorAdmin)

class ContractAdmin(admin.ModelAdmin):
	list_display = ('vendor','contractName','dateRegistered','dateExpiry','file')
admin.site.register(Contract, ContractAdmin)

class LicenseAdmin(admin.ModelAdmin):
	list_display = ('vendor','licenseName','dateRegistered', 'dateExpiry', 'file')
admin.site.register(License, LicenseAdmin)
