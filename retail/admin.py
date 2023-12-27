from django.contrib import admin

from retail.models import Retail, Store, Contacts, Products


# Register your models here.
@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'sp', 'opened_date', 'factory')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'store_name', 'debt_to_supplier', 'creating_date')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('mail', 'country', 'city', 'street', 'house_num', 'store')
    list_filter = ('city',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'to_market_date', 'store')
