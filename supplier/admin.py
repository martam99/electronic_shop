from django.contrib import admin

from supplier.models import Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    fields = ('fullname', 'mail', 'phone')