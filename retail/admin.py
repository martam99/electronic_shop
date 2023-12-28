from django.contrib import admin
from django.db.models import QuerySet
from retail.models import Retail, Store, Contacts, Products


# Register your models here.
@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'sp', 'opened_date', 'factory')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'store_name', 'debt_to_supplier', 'creating_date')
    actions = ['depth_clearer']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def depth_clearer(self, request, queryset: QuerySet):
        queryset.update(debt_to_supplier=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('mail', 'country', 'city', 'street', 'house_num', 'store')
    list_filter = ('city',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'to_market_date', 'store')
