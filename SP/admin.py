from django.contrib import admin

from SP.models import SP


# Register your models here.
@admin.register(SP)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'mail', 'phone')
