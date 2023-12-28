from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        active_employee = Group.objects.create(name='Active_employee')
        p1 = Permission.objects.get(codename='view_factory')
        p2 = Permission.objects.get(codename='view_retail')
        p3 = Permission.objects.get(codename='view_store')
        p4 = Permission.objects.get(codename='view_sp')
        p5 = Permission.objects.get(codename='view_supplier')
        active_employee.permissions.add(p1, p2, p3, p4, p5)
